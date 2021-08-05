import logging

from zgw_consumers.models import Service

logger = logging.getLogger(__name__)


def get_auth(url: str) -> dict:
    client = Service.get_client(url)
    return client.auth_header
