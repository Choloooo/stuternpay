from django.urls import path
from .views import add_beneficiary

urlpatterns = [
    path("add_beneficiary/", add_beneficiary, name="add_beneficiary"),
    # Add other URL patterns as needed
]
