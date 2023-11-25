# urls.py

from django.urls import path
from .views import BusinessCreateView

urlpatterns = [
    path("create/", BusinessCreateView.as_view(), name="create_business"),
    # Add more URLs as needed
]
