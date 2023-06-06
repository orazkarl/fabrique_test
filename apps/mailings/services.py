import requests
from django.conf import settings

from django.db.models import Q

from apps.client.models import Client
from apps.mailings import MessageStatusses
from apps.mailings.models import Mailing, Message


def send_mailings(pk: int):
    try:
        mailing = Mailing.objects.get(pk=pk)
    except Mailing.DoesNotExist:
        raise Mailing.DoesNotExist
    clients = Client.objects.all()
    if mailing.tag_filter and mailing.phone_code_filter:
        clients = clients.filter(
            Q(phone_code=mailing.phone_code_filter) | Q(tag=mailing.tag_filter)
        )
    elif mailing.tag_filter:
        clients = clients.filter(tag=mailing.tag_filter)
    elif mailing.phone_code_filter:
        clients = clients.filter(phone_code=mailing.phone_code_filter)

    for client in clients:
        message = Message.objects.create(
            mailing=mailing,
            client=client
        )
        data = {
            "id": message.pk,
            "phone": client.phone_number.as_e164,
            "text": mailing.message
        }
        headers = {
            'Authorization': f'Bearer {settings.SMS_SERVICE_AUTH_TOKEN}',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(url=settings.SMS_SERVICE_URL + str(message.pk), headers=headers, json=data)
            if response.status_code == 200:
                message.status = MessageStatusses.SENT.value
                message.save(update_fields=['status'])
        except:
            message.status = MessageStatusses.FAILED.value
            message.save(update_fields=['status'])
