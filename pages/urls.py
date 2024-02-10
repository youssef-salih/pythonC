from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_pages, {'pagename': ''}, name='index_pages'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.index_pages, name='index_pages'),
]
