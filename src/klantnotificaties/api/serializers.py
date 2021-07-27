import logging

from rest_framework import serializers

from ..datamodel.models import KlantNotificatie


logger = logging.getLogger(__name__)


class KlantNotificatieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = KlantNotificatie
        fields = ("url", "klant", "productaanvraag", "bericht", "kanaal",)
        extra_kwargs = {"url": {"lookup_field": "uuid"}}
