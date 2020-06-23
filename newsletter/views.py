from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect, render

from . import forms


def index(request):
    """
    Index view for newsletter app
    """
    form = forms.SubscriptionForm(data=request.POST or None)

    success_url = getattr(settings, "NEWSLETTER_SUCCESS_URL", "newsletter:index")
    template_name = getattr(settings, "NEWSLETTER_TEMPLATE", "./newsletter_index.html")

    if form.is_valid():
        form.save()
        return redirect(reverse(success_url) + "?thanks")

    return render(
        request,
        template_name,
        {"form": form, "thanks": "thanks" in request.GET},
    )
