import pytest

from django.test import Client
from django.urls import resolve, reverse

from . import conftest


@pytest.mark.django_db
class TestIndexView:
    def test_index_url(self):
        """
        Test newsletter index url
        """
        assert reverse("newsletter:index") == "/newsletter/"
        assert resolve("/newsletter/").view_name == "newsletter:index"

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
        assert response.url == "/newsletter/?thanks"
