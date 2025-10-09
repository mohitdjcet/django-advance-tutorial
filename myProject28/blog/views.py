from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['username'] = 'mohit'
    request.session['course'] = 'Django full course'
    return HttpResponse("Session data saved successfully.")

def get_session(request):
    username = request.session.get('username','Guest')
    course = request.session.get('course','Not enrolled')
    return HttpResponse(f"Welcome : {username}, You are learning: {course}")

def delete_session(request):
    # try:
    #     del request.session['username']
    #     del request.session['course']
    # except KeyError:
    #     pass
    # return HttpResponse("Session data deleted successfully.")
    request.session.flush() # This will delete all session data
    return HttpResponse("All session data deleted successfully.")