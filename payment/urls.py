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
    exchange_rate,
    process_payment,
    user_transaction
)

urlpatterns = [
    path("make_payment/", PaymentView.as_view(), name="make_payment"),
    path("payment_details/", payment_details, name="payment_details"),
    path("send_details/", payment_confirmation, name="payment_confirmation"),
    path("payment_method/", payment_method, name="payment_method"),
    path("exchange_rate", exchange_rate, name="exchange_rate"),
    path("pay-by-card/", pay_by_card, name="pay_by_card"),
    path("pay-by-transfer/", pay_by_transfer, name="pay_by_transfer"),
    path("transaction-processing/", trans_process, name="transaction"),
    path('process_payment/', process_payment, name='process_payment'),
    path('user_transaction/', user_transaction, name='user_transaction'),
    
    # Add other URLs as needed
]
