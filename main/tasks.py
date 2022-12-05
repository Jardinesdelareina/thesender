from django.core.mail import send_mail
from django.conf import settings
from config.celery import app
from celery import shared_task
from .service import record_data
from .models import Recipient

@shared_task()
# Переносимый task, не зависящий от app
def write_file(email):
    # Запись данных в файл .txt
    record_data(email)
    return True

@app.task(bind=True)
# task, завищящий от приложения   
def periodic_send(self):
    # Периодическая рассылка по адресам, сохраненным в базе данных
    try:
        for recipient in Recipient.objects.all():
            send_mail(
                'Вы подписаны на рассылку',
                'Вы будете получать письма с периодичностью в пять минут.',
                settings.EMAIL_HOST_USER,
                [recipient.email],
                fail_silently=False,
            )
    except Exception as e:
        # В случае ошибки повторится через 60 секунд
        raise self.retry(e=e, countdown=60)