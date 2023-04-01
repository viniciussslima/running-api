from django.contrib import admin

from .models import Asset, Event

admin.site.register(Event)
admin.site.register(Asset)
