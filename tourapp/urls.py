from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from tourapp import views


urlpatterns = [
    url(r'^tourlist/$', views.TourpointList.as_view()),
    url(r'^tourdetails/(?P<pk>[0-9]+)/$', views.TourpointDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)