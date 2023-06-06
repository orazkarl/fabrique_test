from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.core.models import TimestampModel


class Client(TimestampModel):
    phone_number = PhoneNumberField(verbose_name='Номер телефона')
    phone_code = models.PositiveIntegerField(verbose_name='Код мобильного оператора')
    tag = models.CharField(verbose_name='Тeг', max_length=50, blank=True)
    timezone = models.CharField(verbose_name='Часовой пояс', max_length=10)

    def __str__(self):
        return f'Клиент: {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
