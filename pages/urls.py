from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pages, name="index_pages"),
]
