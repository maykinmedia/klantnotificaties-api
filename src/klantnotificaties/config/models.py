from django.db import models
from django.utils.translation import gettext_lazy as _

from solo.models import SingletonModel
from zgw_consumers.constants import APITypes


class ServiceConfiguration(SingletonModel):
    contactmomenten_service = models.OneToOneField(
        "zgw_consumers.Service",
        verbose_name=_("Contactmomenten API"),
        on_delete=models.PROTECT,
        limit_choices_to={"api_type": APITypes.cmc},
        null=True,
        help_text=_(
            "Contactmomenten API in which CONTACTMOMENTen will be created "
            "when a KlantNotificatie is created."
        )
    )
