from django.shortcuts import redirect

from . import forms


def index(request):
    """
    Index view for newsletter app
    """
    form = forms.SubscriptionForm(data=request.POST or None)

    url = request.META.get("HTTP_REFERER", "/")

    if form.is_valid():
        form.save()
        return redirect(f"{url}?newsletter")

    return redirect(url)
