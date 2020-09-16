from newsletter import models

from . import conftest


class TestSubscription:
    def test_subscription_instance(self, subscription_instance):
        """
        Test for subscription instance
        """
        assert str(subscription_instance) == "Subscription for john@doe.com"
