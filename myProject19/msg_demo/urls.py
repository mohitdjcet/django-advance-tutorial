from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_msg, name='show_msg'),
]