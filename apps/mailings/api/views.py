from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.mailings.api.serializers import MailingSerializer, MessageSerializer, MailingStatsSerializer
from apps.mailings.models import Mailing, Message


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(detail=True, methods=['get'])
    def mailing_detail_stats(self, request, pk=None):
        queryset = self.get_queryset()
        mailing = get_object_or_404(queryset, pk=pk)
        serializer = MailingStatsSerializer(mailing)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def mailings_stats(self, request):
        queryset = self.get_queryset()
        serializer = MailingStatsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
