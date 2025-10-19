from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

def users_list(request):
    users = cache.get('users_list')

    if not users:
        print("Cache miss: querying database for users.")
        users = UserProfile.objects.all()
        cache.set('users_list', users, timeout=60)  # Cache for 60 seconds
    else:
        print("Cache hit: retrieved users from cache.")

    return render(request, 'users_list.html', {'users': users})
