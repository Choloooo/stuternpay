# payments/urls.py

from django.urls import path
from .views import (
    PaymentView,
    payment_details,
    payment_confirmation,
    payment_method,
    pay_by_card,
    pay_by_transfer,
    trans_process,
)

urlpatterns = [
    path("make_payment/", PaymentView.as_view(), name="make_payment"),
    path("payment_details/", payment_details, name="payment_details"),
    path("send_details/", payment_confirmation, name="payment_confirmation"),
    path("payment_method/", payment_method, name="payment_method"),
    path("pay-by-card/", pay_by_card, name="pay_by_card"),
    path("pay-by-transfer/", pay_by_transfer, name="pay_by_transfer"),
    path("transaction-processing/", trans_process, name="transaction"),
    # Add other URLs as needed
]
