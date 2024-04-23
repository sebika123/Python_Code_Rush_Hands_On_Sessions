from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):

    list_display = ('recipient_email', 'scheduled_time', 'message')

admin.site.register(Event, EventAdmin)