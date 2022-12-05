from django.db import models


class Recipient(models.Model):
    # Модель получателя рассылки
    email = models.EmailField('Email', max_length=100, unique=True)

    def __str__(self):
        return self.email
