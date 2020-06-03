import pytest
from newsletter.cms_apps import NewsletterApp


@pytest.importorskip("django.settings.INSTALLED_APPS")
class TestNewsletterApp:
    """
    Test case for the EventsApp
    """

    def test_get_urls_method(self):
        """
        Test get_urls method on the ContactApp class
        """

        assert NewsletterApp().get_urls() == ["contact.urls"]
