# transactions/admin.py

from django.contrib import admin
from .models import BankAccount, Reason


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ["account_name", "account_number", "bank_name"]
    search_fields = ["account_name", "account_number", "bank_name"]


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
