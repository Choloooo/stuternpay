from django.contrib import admin
from .models import Beneficiary


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "bank_name",
        "country",
        "swift_code",
        "iban",
    )  # Display these fields in the admin list view
    search_fields = [
        "name",
        "account_number",
        "bank_name",
        "country",
    ]  # Add fields for searching in the admin interface
    list_filter = [
        "user",
        "country",
    ]  # Add filters for these fields in the admin interface
