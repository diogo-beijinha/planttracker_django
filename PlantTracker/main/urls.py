from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name="index"),
    # re_path(r'^accounts/login/$', views.index),
    # re_path(r'^login/$', views.index, name="index"),
    path("home/", views.home, name="home"),
]
