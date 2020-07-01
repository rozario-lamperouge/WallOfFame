from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
			path('',views.Students, name='Students'),
			path('home/',views.Students, name='Students'),
			path('reviews/',views.Reviews, name='Reviews'),
]