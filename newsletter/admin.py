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
    ]
    readonly_fields = ["first_name", "last_name", "email"]
    fieldsets = [
        (None, {"fields": ["first_name", "last_name", "email"]}),
        (
            "Meta Data",
            {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
        ),
    ]
