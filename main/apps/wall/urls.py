from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^message$', views.message),
    url(r'^comment$', views.comment),
    url(r'^logout$', views.logout)
   
]