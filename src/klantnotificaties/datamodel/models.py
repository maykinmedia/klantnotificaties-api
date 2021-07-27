import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class KlantNotificatie(models.Model):
    uuid = models.UUIDField(
        unique=True, default=uuid.uuid4, help_text="Unieke resource identifier (UUID4)"
    )
    klant = models.URLField(
        _("klant"),
        help_text=_("URL-referentie naar de KLANT (in de Klanten API)"),
        max_length=1000,
    )
    productaanvraag = models.URLField(
        _("productaanvraag"),
        help_text=_("URL-referentie naar de ProductAanvraag (in de Objecten API) van de KLANT"),
        max_length=1000,
    )
    bericht = models.TextField(
        _("bericht"),
        help_text=_("Het bericht voor de klant"),
    )

    class Meta:
        verbose_name = "klantnotificatie"
        verbose_name_plural = "klantnotificaties"

