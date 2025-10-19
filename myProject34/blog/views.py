from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

def user_profile_list(request):
    users_data = cache.get('users_data')

    if users_data is None:
        print("Fetching data from database")
        users_data = UserProfile.objects.all()
        cache.set('users_data', users_data) 
    else:
        print("Fetching data from cache")

    return render(request, 'user_profile_list.html', {'users': users_data})
