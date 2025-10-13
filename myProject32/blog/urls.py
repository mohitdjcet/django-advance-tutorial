from django.urls import path
from . import views

urlpatterns = [
    path('bulk-email/', views.send_bulk_email, name='bulk-email'),
]