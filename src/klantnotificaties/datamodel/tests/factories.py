import factory
import factory.fuzzy

from ..models import KlantNotificatie


class KlantNotificatieFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = KlantNotificatie
