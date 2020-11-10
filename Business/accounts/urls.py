
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
   # path('coming_soon/',views.coming_soon,name="coming_soon"),
    path('register',views.register,name="register"),
    
]
