from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect, render

from . import models, forms

__all__ = ["NewsletterPlugin"]


@plugin_pool.register_plugin
class NewsletterPlugin(CMSPluginBase):
    """
    Plugin for newsletter
    """

    name = "Newsletter plugin"
    render_template = "newsletter/plugin.html"

    success_url = getattr(settings, "NEWSLETTER_SUCCESS_URL", "newsletter:index")
    http_referer = getattr(settings, "NEWSLETTER_HTTP_REFERER", False)

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        form = forms.SubscriptionForm(None)
        context.update({"form": form})
        return context
