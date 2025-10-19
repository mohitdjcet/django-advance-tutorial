from django.shortcuts import render
from .models import YouTubeUser
from django.core.cache import cache

def users_list(request):
    users = cache.get('users_data') # Try to get data from cache

    if not users:
        print("Cache miss: Fetching data from database")
        users = YouTubeUser.objects.all()
        cache.set('users_data', users, timeout=60) # Cache data for 60 seconds
    else:
        print("Cache hit: Fetching data from cache")

    return render(request, 'users_list.html', {'users': users})