from django.contrib import admin
from django.urls import path
from build import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/',views.delete,name='delete'),
   
]
