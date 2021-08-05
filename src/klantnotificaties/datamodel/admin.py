from django.contrib import admin

from .models import KlantNotificatie


@admin.register(KlantNotificatie)
class KlantNotificatieAdmin(admin.ModelAdmin):
    list_display = ("uuid", "klant", "productaanvraag", "bericht",)
