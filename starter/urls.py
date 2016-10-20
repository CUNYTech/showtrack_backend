"""starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    # '^$' = empty string
    # url(r'^$', views.hello_world, name='hello_world'),
    url(r'^$', views.HelloWorld.as_view(), name='hello_world'),
    url(r'^api/v1/search/(?P<show>.+)/$', views.SearchView.as_view()),
    # url(r'^api/v1/details/', views.details),
    url(r'^api/v1/details/(?P<show>.+)/$', views.DetailList.as_view()),
    url(r'^api/v1/page/(?P<page_num>\d+)', views.test),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/courses/', include('courses.urls', namespace='courses')),
    url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/v2/search/(?P<show>.+)/?$', views.SearchViewV2.as_view()),
    url(r'^api/v2/single/(?P<show>.+)/?$', views.SingleSearchV2.as_view()),
    url(r'^api/v2/shows/(?P<id>\d+)/?$', views.IDSearchV2.as_view()),
    url(r'^api/v2/shows/(?P<id>\d+)/episodes/?$', views.ShowEpisodes.as_view()),
    url(r'^', include('watchList.urls', namespace='watchList'))
]

urlpatterns += staticfiles_urlpatterns()