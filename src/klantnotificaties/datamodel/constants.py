from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class Kanaal(DjangoChoices):
    email = ChoiceItem(
        "email", _("Email")
    )
    sms = ChoiceItem(
        "sms", _("SMS")
    )
