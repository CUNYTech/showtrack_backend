from django.conf.urls import url
from . import views

urlpatterns = [
    # '^$' = empty string
    # url(r'^$', views.course_list, name="courses"),
    url(r'^$', views.ListCourse.as_view(), name="course_list"),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail),
    url(r'(?P<pk>\d+)/$', views.course_detail),
]