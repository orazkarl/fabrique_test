from rest_framework import routers

from apps.client.api.views import ClientViewSet
from apps.mailings.api.views import MailingViewSet, MessageViewSet

router = routers.DefaultRouter()

router.register('clients', ClientViewSet, basename='clients')
router.register('mailings', MailingViewSet, basename='mailings')
router.register('messages', MessageViewSet, basename='messages')
