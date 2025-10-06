from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Home Page!")
