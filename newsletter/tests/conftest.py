import pytest

from newsletter import models


@pytest.fixture
def subscription_instance():
    return models.Subscription(
        first_name="John", last_name="doe", email="john@doe.com",
    )
