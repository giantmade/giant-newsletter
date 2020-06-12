from newsletter.cms_apps import NewsletterApp


class TestNewsletterApp:
    """
    Test case for the EventsApp
    """

    def test_get_urls_method(self):
        """
        Test get_urls method on the ContactApp class
        """

        assert NewsletterApp().get_urls() == ["newsletter.urls"]
