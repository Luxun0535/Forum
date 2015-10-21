from django.conf.urls import patterns, include, url
from verification import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),


]
