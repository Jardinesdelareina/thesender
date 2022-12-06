from django.db import models


class Subscriber(models.Model):
    # Модель получателя рассылки
    email = models.EmailField('Email', max_length=100, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
