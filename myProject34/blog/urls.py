from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile_list, name='user_profile_list'),
]