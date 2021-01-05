from .forms import SubscriptionForm


def subscription_form(request):
    return {"subscription_form": SubscriptionForm()}
