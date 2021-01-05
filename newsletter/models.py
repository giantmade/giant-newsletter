from django.db import models

from mixins.models import TimestampMixin


class Subscription(TimestampMixin):
    """
    Represents a subscription object
    """

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=255, blank=True)
    accepted_terms = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        """
        String representation
        """
        return f"Subscription for {self.email}"
