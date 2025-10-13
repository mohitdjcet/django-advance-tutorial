from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

# def send_test_email(request):
#     subject = "Welcome to My Blog"
#     message = "Thank you for subscribing to My Blog!"
#     from_email = "mohitdecodes@gmail.com"
#     recipient_list = ["mohit.djcet@gmail.com"]

#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("Test email sent successfully!")

def send_test_email(request):
    subject = "Welcome to My Blog"
    message = render_to_string('email/welcome_email.html', {
        'username': 'Mohit',
        'course': 'Django Tutorial',
        })
    email = EmailMessage(
        subject,
        message,
        "mohitdecodes@gmail.com",
        ["mohit.djcet@gmail.com"]
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.send()
    return HttpResponse("Test email sent successfully!")