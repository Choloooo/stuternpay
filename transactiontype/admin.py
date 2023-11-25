# transactions/admin.py

from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction_type"]  # Adjust based on your model fields
    search_fields = [
        "transaction_type"
    ]  # Add fields for searching in the admin interface
    list_filter = [
        "transaction_type"
    ]  # Add filters for these fields in the admin interface
