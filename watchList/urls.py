from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'watchlist/?$', views.WatchListCreateAPIView.as_view()),
]