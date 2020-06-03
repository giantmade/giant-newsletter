from django.forms import ModelForm

from . import models


class SubscriptionForm(ModelForm):
    """
    Modelform for subscription model
    """

    class Meta:
        model = models.Subscription
        fields = ["first_name", "last_name", "email"]
