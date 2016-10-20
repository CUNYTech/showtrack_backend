from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    # url(r'login/$', views.login_view),
    url(r'login/', obtain_jwt_token),
    # url(r'signup/$', views.signup_view),
    url(r'register/?$', views.UserCreateAPIView.as_view()),
    url(r'users/?$', views.UserListAPIView.as_view()),
    url(r'profile/?$', views.UserDetailView.as_view())
]