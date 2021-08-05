import logging

from django.conf import settings
from rest_framework import serializers
from vng_api_common.validators import ResourceValidator, URLValidator

from ..datamodel.models import KlantNotificatie
from .auth import get_auth


logger = logging.getLogger(__name__)


class KlantNotificatieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KlantNotificatie
        fields = (
            "url",
            "klant",
            "productaanvraag",
            "bericht",
            "kanaal",
        )
        extra_kwargs = {
            "url": {"lookup_field": "uuid"},
            "klant": {
                "validators": [
                    ResourceValidator(
                        "Klant", settings.KLANTEN_API_SPEC, get_auth=get_auth
                    )
                ]
            },
            "productaanvraag": {"validators": []},
        }
