from django.contrib import admin
from django.urls import path, include
from .views import * 



urlpatterns = [
    path('', index, name = 'index'),
    path('home/', home, name = 'home'),
    path('detail/<int:id>/', detail, name ='detail'),
    path('new/', new, name = 'new'),
    path('create/', create, name = 'create'),
]
