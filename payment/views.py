# payments/views.py

from django.shortcuts import render
from django.views import View
from .forms import PaymentForm


class PaymentView(View):
    template_name = "payments/make_payment.html"

    def get(self, request, *args, **kwargs):
        form = PaymentForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process the form data (save to the database, perform payment, etc.)
            selected_payment_method = form.cleaned_data["payment_method"]
            # Do something with the selected payment method

            return render(
                request,
                "payments/success.html",
                {"selected_payment_method": selected_payment_method},
            )
            # Redirect to success page or another view with the selected payment method
        return render(request, self.template_name, {"form": form})


def payment_details(request):
    return render(request, "payment_details.html")


def payment_confirmation(request):
    return render(request, "paymentconfirmation.html")


def payment_method(request):
    return render(request, "selectpaymentmethod.html")


def pay_by_card(request):
    # Your logic for handling payments by card
    return render(request, "cardpayment.html")


def pay_by_transfer(request):
    # Your logic for handling payments by transfer
    return render(request, "transfertobankoption.html")


def trans_process(request):
    # Your logic for handling payments by transfer
    return render(request, "transactionprocessing.html")


def exchange_rate(request):
    # Your logic for handling payments by transfer
    return render(request, "exchange_rate.html")
