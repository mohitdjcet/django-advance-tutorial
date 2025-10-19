from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list, name='users'),
    path('clear/', views.clear_catch, name='clear_catch'), 
]

