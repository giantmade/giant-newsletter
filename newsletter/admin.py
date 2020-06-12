from django.conf import settings
from django.contrib import admin

from . import models


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Admin for subscription model
    """

    list_display = [
        "email",
        "created_at",
    ] or settings.NEWSLETTER_ADMIN_LIST_DISPLAY

    readonly_fields = ["first_name", "last_name", "email"] or settings.NEWSLETTER_ADMIN_READONLY_FIELDS

    fieldsets = [
        (None, {"fields": ["first_name", "last_name", "email"]}),
        (
            "Meta Data",
            {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
        ),
    ] or settings.NEWSLETTER_ADMIN_FIELDSETS
