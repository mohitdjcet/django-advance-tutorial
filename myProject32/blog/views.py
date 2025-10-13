from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string

# def send_bulk_email(request):
#     messages1 = ('Wecome User 1', 'Hello User 1, welcome to our platform.', 'mohitdecodes@gmail.com', ['mohit.djcet@gmail.com'])
#     messages2 = ('Wecome User 2', 'Hello User 2, welcome to our platform.', 'mohitdecodes@gmail.com', ['mohit.djcet1@gmail.com'])
#     messages3 = ('Wecome User 3', 'Hello User 3, welcome to our platform.', 'mohitdecodes@gmail.com', ['mohit.djcet2@gmail.com'])

#     send_mass_mail((messages1, messages2, messages3), fail_silently=False)

#     return HttpResponse("Bulk emails sent successfully!")

def send_bulk_email(request):
    subject = "Welcome to Our Platform"
    from_email = "mohitdecodes@gmail.com"
    recipient_list = ["mohit.djcet@gmail.com", "mohit.djce2@gmail.com"]

    html_content = render_to_string('welcome_email.html', {'username': 'Mohit'})


    msg = EmailMultiAlternatives(subject, "Welcome to my Platform", from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    # msg.attach_file('path/to/your/attachment.pdf')  # Optional: Attach a file
    msg.send()

    return HttpResponse("Bulk emails sent successfully!")