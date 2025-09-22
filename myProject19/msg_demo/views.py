from django.shortcuts import render
from django.contrib import messages

def show_msg(request):
    messages.debug(request, 'This is a debug message.')
    messages.info(request, 'This is an info message.')
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')

    return render(request, 'message.html')
