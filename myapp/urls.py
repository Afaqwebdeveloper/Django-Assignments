from django.contrib import admin
from django.urls import path, include
from . import views 

app_name="myapp"

urlpatterns = [
    path("index/", views.index, name='index'),
    path("details/", views.details, name='details'),
]