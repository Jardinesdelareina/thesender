from django.core.mail import send_mail
from django.conf import settings
from config.celery import app
from .service import send
from .models import Recipient

@app.task()
def write_file(email):
    send(email)
    return True

@app.task()
def periodic_send():
    for recipient in Recipient.objects.all():
        send_mail(
            'Вы подписаны на рассылку',
            'Вы будете получать письма с периодичностью в пять минут.',
            settings.EMAIL_HOST_USER,
            [recipient.email],
            fail_silently=False,
        )
