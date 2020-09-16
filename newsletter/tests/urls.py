from django.urls import include, path

""""
Url patterns for testing
"""

urlpatterns = [path("newsletter/", include("newsletter.urls", namespace="newsletter"))]
