from unittest import skip

import requests_mock
from django.conf import settings
from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.tests import reverse
from zgw_consumers.test.schema_mock import mock_service_oas_get

from klantnotificaties.accounts.tests.factories import (
    TokenFactory, UserFactory
)
from klantnotificaties.config.tests.factories import ServiceFactory
from klantnotificaties.datamodel.models import KlantNotificatie
from klantnotificaties.datamodel.tests.factories import KlantNotificatieFactory


class KlantNotificatiesTestCase(APITestCase):
    def setUp(self):
        super().setUp()

        self.user = UserFactory.create()
        self.token = TokenFactory.create(user=self.user)
        self.auth_header = {"HTTP_AUTHORIZATION": f"Token {self.token.key}"}

        ServiceFactory.create(api_root="http://klanten.nl/api/v1")

    @requests_mock.Mocker()
    def test_klantnotificatie_create_success_email_channel(self, m):
        mock_service_oas_get(m, "http://klanten.nl/api/v1/", "klanten")
        mock_service_oas_get(m, settings.KLANTEN_API_SPEC, "klanten", oas_url=settings.KLANTEN_API_SPEC)

        m.get(
            "http://klanten.nl/api/v1/klanten/1",
            json={
                "url": "http://klanten.nl/api/v1/klanten/1",
                "voorkeurskanaal": "email",
                "emailadres": "foo@bar.nl",
            },
        )
        response = self.client.post(
            reverse(KlantNotificatie),
            {
                "klant": "http://klanten.nl/api/v1/klanten/1",
                "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
                "bericht": "foo",
                "kanaal": "email",
            },
            **self.auth_header,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        klantnotificatie = KlantNotificatie.objects.get()

        expected_data = {
            "url": f"http://testserver/api/v1/klantnotificaties/{klantnotificatie.uuid}",
            "klant": "http://klanten.nl/api/v1/klanten/1",
            "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
            "bericht": "foo",
            "kanaal": "email",
        }
        self.assertDictEqual(response.data, expected_data)

        # Verify that the Klanten OAS and the klant URL were retrieved
        self.assertEqual(len(m.request_history), 2)

        klanten_oas_get, klant_get = m.request_history
        self.assertEqual(klanten_oas_get.method, "GET")
        self.assertEqual(klanten_oas_get.url, "http://klanten.nl/api/v1/schema/openapi.yaml?v=3")

        self.assertEqual(klant_get.method, "GET")
        self.assertEqual(klant_get.url, "http://klanten.nl/api/v1/klanten/1")

        # Verify that the email was sent
        self.assertEqual(len(mail.outbox), 1)
        sent_email = mail.outbox[0]

        self.assertEqual(sent_email.from_email, "klantnotificaties@example.com")
        self.assertEqual(sent_email.to, ["foo@bar.nl"])
        self.assertEqual(sent_email.subject, "Notification")
        self.assertIn("foo", sent_email.body)

    @skip("SMS channel not implemented yet")
    @requests_mock.Mocker()
    def test_klantnotificatie_create_success_sms_channel(self, m):
        mock_service_oas_get(m, "http://klanten.nl/api/v1/", "klanten")

        m.get(
            "http://klanten.nl/api/v1/klanten/1",
            json={
                "url": "http://klanten.nl/api/v1/klanten/1",
                "voorkeurskanaal": "sms",
                "telefoonnummer": "0612345678",
            },
        )
        response = self.client.post(
            reverse(KlantNotificatie),
            {
                "klant": "http://klanten.nl/api/v1/klanten/1",
                "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
                "bericht": "foo",
                "kanaal": "sms",
            },
            **self.auth_header,
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        klantnotificatie = KlantNotificatie.objects.get()

        expected_data = {
            "url": f"http://testserver/api/v1/klantnotificaties/{klantnotificatie.uuid}",
            "klant": "http://klanten.nl/api/v1/klanten/1",
            "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
            "bericht": "foo",
            "kanaal": "sms",
        }
        self.assertDictEqual(response.data, expected_data)

        # Verify that the Klanten OAS and the klant URL were retrieved
        self.assertEqual(len(m.request_history), 2)

        klanten_oas_get, klant_get = m.request_history
        self.assertEqual(klanten_oas_get.method, "GET")
        self.assertEqual(klanten_oas_get.url, "http://klanten.nl/api/v1/schema/openapi.yaml?v=3")

        self.assertEqual(klant_get.method, "GET")
        self.assertEqual(klant_get.url, "http://klanten.nl/api/v1/klanten/1")

        # Verify that the SMS was sent
        pass

    def test_klantnotificatie_list_success(self):
        klantnotificatie1 = KlantNotificatieFactory.create(
            klant="http://klanten.nl/api/v1/klanten/1",
            productaanvraag="http://objecten.nl/api/v1/objecten/1",
            bericht="foo",
            kanaal="email",
        )
        klantnotificatie2 = KlantNotificatieFactory.create(
            klant="http://klanten.nl/api/v1/klanten/2",
            productaanvraag="http://objecten.nl/api/v1/objecten/2",
            bericht="bar",
            kanaal="sms",
        )

        response = self.client.get(reverse(KlantNotificatie), **self.auth_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)

        self.assertDictEqual(response.data[0], {
            "url": f"http://testserver/api/v1/klantnotificaties/{klantnotificatie1.uuid}",
            "klant": "http://klanten.nl/api/v1/klanten/1",
            "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
            "bericht": "foo",
            "kanaal": "email",
        })
        self.assertDictEqual(response.data[1], {
            "url": f"http://testserver/api/v1/klantnotificaties/{klantnotificatie2.uuid}",
            "klant": "http://klanten.nl/api/v1/klanten/2",
            "productaanvraag": "http://objecten.nl/api/v1/objecten/2",
            "bericht": "bar",
            "kanaal": "sms",
        })

    def test_klantnotificatie_read_success(self):
        klantnotificatie = KlantNotificatieFactory.create(
            klant="http://klanten.nl/api/v1/klanten/1",
            productaanvraag="http://objecten.nl/api/v1/objecten/1",
            bericht="foo",
            kanaal="email",
        )

        response = self.client.get(reverse(klantnotificatie), **self.auth_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertDictEqual(response.data, {
            "url": f"http://testserver/api/v1/klantnotificaties/{klantnotificatie.uuid}",
            "klant": "http://klanten.nl/api/v1/klanten/1",
            "productaanvraag": "http://objecten.nl/api/v1/objecten/1",
            "bericht": "foo",
            "kanaal": "email",
        })
