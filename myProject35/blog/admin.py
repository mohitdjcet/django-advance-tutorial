from django.contrib import admin
from .models import UserList

@admin.register(UserList)
class UserListAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscriber')
