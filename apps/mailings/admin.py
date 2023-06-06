from django.contrib import admin

from apps.mailings.models import Mailing, Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_datetime', 'end_datetime', 'phone_code_filter', 'tag_filter')
    list_filter = ('start_datetime', 'end_datetime', 'phone_code_filter', 'tag_filter')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing', 'client')
    list_filter = ('status', )
