from contextlib import contextmanager
from typing import Union, List, Dict

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from mail_editor.helpers import find_template
from zgw_consumers.models import Service


class NotificationError(Exception):
    pass


@contextmanager
def _fake_atomic():
    yield


def conditional_atomic(wrap: bool = True):
    """
    Wrap either a fake or real atomic transaction context manager.
    """
    return transaction.atomic if wrap else _fake_atomic


def email_handler(klant_data: dict, message: str):
    recipient = klant_data["emailadres"]

    # TODO accept template name parameter via API
    template = find_template("default")

    # TODO supply from_email? subject context should also be supplied via API
    template.send_email([recipient], {"content": message}, subj_context={"subject": "Notification"})


def sms_handler(klant_data: dict, bericht: str):
    recipient = klant_data["telefoonnummer"]

    # TODO send sms
    raise NotImplementedError


class KlantNotificatieMixin:
    notifications_wrap_in_atomic_block = True

    channel_handler_mapping = {
        "email": email_handler,
        "sms": sms_handler,
    }

    def create(self, request, *args, **kwargs):
        with conditional_atomic(self.notifications_wrap_in_atomic_block)():
            response = super().create(request, *args, **kwargs)
            self.send_notification(response.data)
            return response

    def send_notification(self, data: Union[List, Dict]):
        client = Service.get_client(data["klant"])

        if not client:
            raise NotificationError(_("Could not find a Service for klant: {}").format(data["klant"]))

        klant_uuid = data["klant"].split("/")[-1]
        klant_data = client.retrieve("klant", uuid=klant_uuid)

        # TODO voorkeurskanaal not implemented yet in Klanten API
        # TODO use override from ProductAanvraag?
        kanaal = data["kanaal"]

        handler = self.channel_handler_mapping[kanaal]

        handler(klant_data, data["bericht"])
