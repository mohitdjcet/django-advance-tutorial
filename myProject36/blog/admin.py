from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserListAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscribers')
