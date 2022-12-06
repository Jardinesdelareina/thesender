from django.core.mail import send_mail
from django.conf import settings
from config.celery import app
from .models import Subscriber
from .service import record_data

@app.task()
def send_worker(user_email):
    send_mail(
        'Здравствуйте!',
        'Вы подписаны на рассылку.',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )
    record_data(user_email)

@app.task()
def send_beat():
    # Периодическая рассылка по адресам, сохраненным в базе данных
    for subscriber in Subscriber.objects.all():
        send_mail(
            'Здравствуйте!',
            'Вы будете получать письма с периодичностью в пять минут.',
            settings.EMAIL_HOST_USER,
            [subscriber.email],
            fail_silently=False,
        )
