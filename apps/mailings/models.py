from apscheduler.schedulers.background import BackgroundScheduler
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from apps.client.models import Client
from apps.core.models import TimestampModel
from apps.mailings import MessageStatusses


class Mailing(TimestampModel):
    start_datetime = models.DateTimeField(
        verbose_name='Дата и время начала рассылки'
    )
    end_datetime = models.DateTimeField(
        verbose_name='Дата и время окончания рассылки'
    )
    message = models.TextField(verbose_name='Сообщение')
    phone_code_filter = models.PositiveIntegerField(
        verbose_name='Код мобильного оператора',
        blank=True
    )
    tag_filter = models.CharField(
        verbose_name='Тeг',
        max_length=50,
        blank=True
    )

    @property
    def to_send(self):
        return self.start_datetime <= timezone.now() <= self.end_datetime

    def __str__(self):
        return f'{self.message}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(TimestampModel):
    status = models.CharField(
        verbose_name='Статус',
        max_length=15,
        choices=MessageStatusses.choices,
        default=MessageStatusses.IN_PROGRESS
    )
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Сообщение: {self.pk}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


def scedule_mailing(sender, instance, signal, *args, **kwargs):
    from apps.mailings.services import send_mailings

    run_date = timezone.now() if instance.to_send else instance.start_datetime
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_mailings,
        trigger='date',
        run_date=run_date,
        args=[instance.pk],
        coalesce=True,
        max_instances=1,
        replace_existing=True,
    )
    scheduler.start()


post_save.connect(scedule_mailing, sender=Mailing)