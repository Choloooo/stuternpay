# payments/admin.py

from django.contrib import admin
from .models import Payment, PaymentTransaction


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["payment_method"]




@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'beneficiaryAccountNumber',
        'toCurrency',
        'sendAmount',
        'beneficiaryName',
        'bankName',
        'swift',
        'totalAmountWithFee',
        'iban',
        'feeAmount',
        'fromCurrency',
        'country',
        'recipientAmount'
    ]