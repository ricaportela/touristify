from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tourapp.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', views.login),
    url(r'^home/$', views.home),
    url(r'^logout/$', views.logout)
]
