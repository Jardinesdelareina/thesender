from django.db import models


class Recipient(models.Model):
    # Модель получателя рассылки
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email', max_length=100, unique=True)

    def __str__(self):
        return self.name
