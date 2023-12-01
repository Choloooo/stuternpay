from django.urls import path
from .views import add_beneficiary

urlpatterns = [
    path("beneficiary/", add_beneficiary, name="beneficiary"),
    # Add other URL patterns as needed
]
