import logging

from rest_framework import mixins, viewsets
from vng_api_common.permissions import BaseAuthRequired

from ..datamodel.models import KlantNotificatie
from .scopes import EXAMPLE_SCOPE
from .serializers import KlantNotificatieSerializer

logger = logging.getLogger(__name__)


class KlantNotificatieViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    """
    Describe viewset.

    create:
    Maak een KLANTNOTIFICATIE aan.

    Maak een KLANTNOTIFICATIE aan.

    list:
    Alle KLANTNOTIFICATIEs opvragen.

    Alle KLANTNOTIFICATIEs opvragen.

    retrieve:
    Een specifieke KLANTNOTIFICATIE opvragen.

    Een specifieke KLANTNOTIFICATIE opvragen.
    """

    queryset = KlantNotificatie.objects.all()
    serializer_class = KlantNotificatieSerializer
    lookup_field = "uuid"

    permission_classes = (BaseAuthRequired,)
    required_scopes = {
        "list": EXAMPLE_SCOPE,
        "retrieve": EXAMPLE_SCOPE,
        "create": EXAMPLE_SCOPE,
        "update": EXAMPLE_SCOPE,
        "partial_update": EXAMPLE_SCOPE,
        "destroy": EXAMPLE_SCOPE,
    }
