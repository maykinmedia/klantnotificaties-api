from django.conf import settings

from drf_yasg import openapi

description = """Een API om een Klantnotificaties aan te maken.

Deze API kan aangeroepen worden door andere systemen, om bijvoorbeeld emails naar
klanten te versturen.

**Autorisatie**

Deze API vereist autorisatie. Je kan de
[token-tool](https://ref.tst.vng.cloud/tokens/) gebruiken om JWT-tokens te
genereren.

**Handige links**

* [Aan de slag](https://ref.tst.vng.cloud/ontwikkelaars/)
* ["Papieren" standaard](https://ref.tst.vng.cloud/standaard/)
"""

info = openapi.Info(
    title="Klantnotificaties API",
    default_version=settings.API_VERSION,
    description=description,
    contact=openapi.Contact(
        email="support@maykinmedia.nl",
        url="https://github.com/VNG-Realisatie/gemma-zaken",
    ),
    license=openapi.License(name="EUPL 1.2"),
)
