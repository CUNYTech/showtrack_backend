from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'login/$', views.login_view),
    # url(r'signup/$', views.signup_view),
    url(r'register/$', views.UserCreateAPIView.as_view())
]