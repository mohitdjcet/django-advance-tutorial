from django.urls import path
from . import views

urlpatterns = [
    path('set-cookie/', views.set_cookie, name='set_cookie'),
    path('get-cookie/', views.get_cookie, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie, name='delete_cookie'),
]
