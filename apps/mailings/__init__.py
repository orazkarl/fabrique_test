from django.db.models import TextChoices


class MessageStatusses(TextChoices):
    IN_PROGRESS = 'IN_PROGRESS', 'В процессе'
    SENT = 'SENT', 'Отправлен'
    FAILED = 'FAILED', 'Ошибка'
