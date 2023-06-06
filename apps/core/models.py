import datetime

from django.db import models


class TimestampModel(models.Model):
    created_at: datetime.datetime = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
    )
    changed_at: datetime.datetime = models.DateTimeField(
        "Время последнего изменения", auto_now=True, db_index=True
    )

    class Meta:
        abstract = True
