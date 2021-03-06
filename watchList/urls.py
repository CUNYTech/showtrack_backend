from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'watchlist/?$', views.WatchListCreateAPIView.as_view()),
    url(r'watchlist/list?$', views.ShowWatchList.as_view()),
    url(r'watchlist/update/?$', views.UpdateWatchList.as_view()),
    url(r'watchlist/delete/?$', views.DeleteWatchListShow.as_view())
]