from django.contrib import admin

from apps.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'phone_code', 'tag', 'timezone')
    list_filter = ('phone_code', 'tag')
