from django.urls import reverse
from django.shortcuts import redirect, render

from . import forms


def index(request):
    """
    Index view for newsletter app
    """
    form = forms.SubscriptionForm(data=request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse("newsletter:index") + "?thanks")

    return render(
        request,
        "./newsletter_index.html",
        {"form": form, "thanks": "thanks" in request.GET},
    )
