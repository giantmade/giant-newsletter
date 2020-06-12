import pytest


@pytest.importorskip("django.settings.INSTALLED_APPS")
@pytest.mark.django_db
class TestSubscription:
    # import models here to avoid error
    from newsletter import models

    @pytest.fixture
    def subscription_instance(self):
        return self.models.Subscription.objects.create(
            first_name="John", last_name="doe", email="john@doe.com",
        )

    def test_subscription_instance(self, subscription_instance):
        """
        Test for subscription instance
        """
        subscription = self.models.Subscription.objects.get(
            email=subscription_instance.email
        )

        assert str(subscription) == "Subscription for john@doe.com"
