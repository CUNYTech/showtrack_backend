from django.conf.urls import url
from . import views

urlpatterns = [
    # '^$' = empty string
    url(r'^$', views.course_list)
]