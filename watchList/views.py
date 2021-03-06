import json
import requests
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


from .serializers import WatchListSerializer, ShowSerializer
from .models import WatchList, Show

from starter.views import IDSearchV2

# Create your views here.
class WatchListView(ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class WatchListCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ShowWatchList(ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user.id)
        serializer = WatchListSerializer(queryset, many=True)
        shows = Show.objects.all()
        for show in serializer.data:
            show_serializer = ShowSerializer(shows.filter(id=show['show_id']), many=True)
            if show_serializer.data:
                show['show_details'] = show_serializer.data[0]
            else:
                re = requests.get('http://api.tvmaze.com/shows/{}'.format(show['show_id']))
                re_json = re.json()
                Show.objects.create(id=re_json['id'], content=re_json)
                show_serializer = ShowSerializer(shows.filter(id=re_json['id']), many=True)
                show['show_details'] = show_serializer.data[0]
                # show.update({'show_details': show_serializer.data[0]})

        return Response(serializer.data)

class UpdateWatchList(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def update(self, request, *args, **kwargs):
        print(self.kwargs)
        partial = kwargs.pop('partial', True)
        queryset = self.get_queryset().filter(user=request.user.id, show_id=request.data['show_id'])
        print(queryset)
        instance = WatchList.objects.get(user=request.user.id, show_id=request.data['show_id'])
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class DeleteWatchListShow(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchListSerializer

    def destroy(self, request, *args, **kwargs):
        message = {}
        instance = None
        try:
            instance = WatchList.objects.get(user=request.user.id, show_id=request.data['show_id'])
            message = {'message': 'Show successfully deleted'}
        except ObjectDoesNotExist:
            message = {'error': 'Invalid show ID'}
        self.perform_destroy(instance)
        return Response(message, status=status.HTTP_202_ACCEPTED)