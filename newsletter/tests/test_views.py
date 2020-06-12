import pytest

from django.test import Client
from django.urls import resolve, reverse


@pytest.importorskip("django.settings.INSTALLED_APPS")
class TestIndexView:
    def test_index_url(self):
        """
        Test newsletter index url
        """
        assert reverse("newsletter:index") == "/newsletter/"
        assert resolve("/newsletter/").view_name == "newsletter:index"

    def test_create(self, subscription_instance):
        """
        Test successful subscription submissions ultimate status code
        """
        client = Client()
        response = client.post(
            reverse("newsletter:index"),
            {"email": subscription_instance.email},
            follow=True,
        )
        assert response.status_code == 200

    def test_success_redirect(self, subscription_instance):
        """
        Test successful subscription redirect
        """
        client = Client()

        headers = {"HTTP_REFERER": "/"}
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": subscription_instance.email,
        }

        response = client.post(reverse("newsletter:index"), data, **headers)
        assert response.status_code == 302
        assert response.url == "/"

    def test_fail_redirect(self, subscription_instance):
        """
        Test invalid subscription submission
        """
        client = Client()
        response = client.post(reverse("newsletter:index"), {"email": "invalid"})
        assert response.status_code == 302
