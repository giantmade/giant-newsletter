from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class NewsletterApp(CMSApp):
    """
    Apphook for newsletter
    """

    name = _("Newsletter")
    app_name = "newsletter"

    def get_urls(self, page=None, language=None, **kwargs):
        """
        Return urls for this app
        """
        return ["newsletter.urls"]
