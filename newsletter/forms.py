from django.forms import ModelForm
from django.conf import settings

from . import models


class SubscriptionForm(ModelForm):
    """
    Modelform for subscription model
    """

    required_fields = getattr(settings, "NEWSLETTER_FORM_REQUIRED_FIELDS", [])
    field_placeholders = getattr(settings, "NEWSLETTER_FORM_FIELD_PLACEHOLDERS", {})

    class Meta:
        model = models.Subscription
        fields = getattr(
            settings,
            "NEWSLETTER_FORM_FIELDS",
            ["first_name", "last_name", "email", "company", "accepted_terms"],
        )
        labels = getattr(settings, "NEWSLETTER_FORM_LABELS", None)
        widgets = getattr(settings, "NEWSLETTER_FORM_WIDGETS", None)

    def __init__(self, *args, **kwargs):
        """
        Override the init method to set the customised required fields
        """
        super().__init__(*args, **kwargs)

        # Update the required fields
        for field in self.required_fields:
            self.fields[field].required = True

        # Update field placeholder
        for field, placeholder in self.field_placeholders.items():
            field = self.fields.get(field)
            field.widget.attrs["placeholder"] = placeholder
