from rest_framework import serializers

from apps.mailings import MessageStatusses
from apps.mailings.models import Mailing, Message


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class MailingStatsSerializer(MailingSerializer):
    in_progress = serializers.SerializerMethodField
    failed = serializers.SerializerMethodField()
    sent = serializers.SerializerMethodField()

    def get_in_progress(self, pk):
        return Message.objects.filter(message=pk, status=MessageStatusses.IN_PROGRESS.value).count()

    def get_failed(self, pk):
        return Message.objects.filter(message=pk, status=MessageStatusses.FAILED.value).count()

    def get_sent(self, pk):
        return Message.objects.filter(message=pk, status=MessageStatusses.SENT.value).count()


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
