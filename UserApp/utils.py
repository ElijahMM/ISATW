from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from UserApp.models import User


def register_new_teacher(teacher, domain):
    generate_password = BaseUserManager().make_random_password(length=6)
    print(generate_password)
    new_user = User()
    new_user.first_name = teacher.cleaned_data['first_name']
    new_user.last_name = teacher.cleaned_data['last_name']
    new_user.email = teacher.cleaned_data['email']
    new_user.is_teacher = True
    new_user.set_password(generate_password)
    new_user.save()

    # send email
    to_email = teacher.cleaned_data['email']
    subject = 'Inregistrare profesor'
    content = {
        'first_name': teacher.cleaned_data['first_name'],
        'last_name': teacher.cleaned_data['last_name'],
        'domain': domain,
        'email': teacher.cleaned_data['email'],
        'password': generate_password
    }
    message = render_to_string('emails/send_mail_teacher.html', content)
    send_email = EmailMessage(subject, message, to=[to_email])
    send_email.send()


def delete_user(email):
    try:
        user = User.objects.get(email=email)
        user.delete()
    except Exception:
        pass
