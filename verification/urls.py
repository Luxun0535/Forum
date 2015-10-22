from django.conf.urls import patterns, include, url
from verification import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^weiboLogin/', views.weiboLogin, name='weiboLogin'),
    url(r'^weibo_check/', views.weibo_check, name='weibo_check'),
    url(r'^QQLogin/', views.QQLogin, name='QQLogin'),
    url(r'^QQ_check/', views.QQ_check, name='QQ_check'),
    url(r'^weiboLogin/', views.weiboLogin, name='weiboLogin'),
    url(r'^weibo_check/', views.weibo_check, name='weibo_check'),
]
