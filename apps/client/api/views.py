from rest_framework import viewsets

from apps.client.api.serializers import ClientSerializer
from apps.client.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
