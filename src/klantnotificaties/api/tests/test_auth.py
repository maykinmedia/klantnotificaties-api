from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.tests import reverse

from klantnotificaties.datamodel.models import KlantNotificatie
from klantnotificaties.datamodel.tests.factories import KlantNotificatieFactory


class KlantNotificatiesTestCase(APITestCase):
    def test_klantnotificatie_create_not_authenticated(self):
        response = self.client.post(
            reverse(KlantNotificatie),
            {
                "klant": "http://klanten.nl/api/v1/klanten/1",
                "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
                "bericht": "foo",
                "kanaal": "email",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_klantnotificatie_list_not_authenticated(self):
        response = self.client.get(reverse(KlantNotificatie))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_klantnotificatie_read_not_authenticated(self):
        klantnotificatie = KlantNotificatieFactory.create()
        response = self.client.get(reverse(klantnotificatie))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_klantnotificatie_list_invalid_auth_token(self):
        response = self.client.get(
            reverse(KlantNotificatie), HTTP_AUTHORIZATION="Token 12345"
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
