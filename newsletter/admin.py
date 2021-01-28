from django.conf import settings
from django.contrib import admin

from . import models

from mixins.admin import CSVAdminMixin


@admin.register(models.Subscription)
class SubscriptionAdmin(CSVAdminMixin):
    """
    Admin for subscription model
    """

    list_display = getattr(
        settings, "NEWSLETTER_ADMIN_LIST_DISPLAY", ["email", "created_at"]
    )
    readonly_fields = getattr(
        settings, "NEWSLETTER_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"],
    )
    fieldsets = getattr(
        settings,
        "NEWSLETTER_ADMIN_FIELDSETS",
        [
            (
                None,
                {
                    "fields": [
                        "first_name",
                        "last_name",
                        "email",
                        "company",
                        "accepted_terms",
                    ]
                },
            ),
            (
                "Meta Data",
                {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
            ),
        ],
    )
