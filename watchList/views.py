from django.http import HttpResponse
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