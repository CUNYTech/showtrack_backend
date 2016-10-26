from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import WatchListSerializer
from .models import WatchList

# Create your views here.
class WatchListView(ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class WatchListCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
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