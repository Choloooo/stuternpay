# payments/views.py

from django.shortcuts import render
from django.views import View
from .forms import PaymentForm
from .models import PaymentTransaction
from django.http import HttpResponseServerError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import requests



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

@login_required
def payment_details(request):
    return render(request, "payment_details.html")

@login_required
def payment_confirmation(request):
    return render(request, "paymentconfirmation.html")

@login_required
def payment_method(request):
    return render(request, "selectpaymentmethod.html")

@login_required
def pay_by_card(request):
    # Your logic for handling payments by card
    return render(request, "cardpayment.html")

@login_required
def pay_by_transfer(request):
    # Your logic for handling payments by transfer
    return render(request, "transfertobankoption.html")

@login_required
def trans_process(request):
    # Your logic for handling payments by transfer
    return render(request, "transactionprocessing.html")

@login_required
def exchange_rate(request):
    # Your logic for handling payments by transfer
    return render(request, "exchange_rate.html")


@login_required
@csrf_exempt
def process_payment(request):
    # Retrieve logged-in user
    user = request.user if request.user.is_authenticated else None

    if request.method == 'POST':
        try:
            # Retrieve data from the request body
            data = json.loads(request.body)
            session_data = data.get('data')

            # Create a new PaymentTransaction instance and save it to the database
            # Use the correct field names as per your model
            payment_transaction = PaymentTransaction(
                user=request.user,
                beneficiaryAccountNumber=session_data.get('beneficiaryAccountNumber'),
                toCurrency=session_data.get('toCurrency'),
                sendAmount=session_data.get('sendAmount'),
                beneficiaryName=session_data.get('beneficiaryName'),
                bankName=session_data.get('bankName'),
                swift=session_data.get('swift'),
                totalAmountWithFee=session_data.get('totalAmountWithFee'),
                iban=session_data.get('iban'),
                feeAmount=session_data.get('feeAmount'),
                fromCurrency=session_data.get('fromCurrency'),
                country=session_data.get('country'),
                recipientAmount=session_data.get('recipientAmount'),
            )
            payment_transaction.save()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


@login_required
def user_transaction(request):
    user_transaction = PaymentTransaction.objects.filter(user=request.user)
    for transaction in user_transaction:
        print(f"Account Number: {transaction.beneficiaryAccountNumber}")

    return render(request, 'user_transaction.html', {'user_transaction': user_transaction})





def get_exchange_rate(request):
    from_currency = request.GET.get('from_currency')

    if not from_currency:
        return JsonResponse({'error': 'from_currency parameter is missing'}, status=400)

    api_url = f'https://v6.exchangerate-api.com/v6/b660905cac3ae9db40d489d8/latest/{from_currency}'

    try:
        response = requests.get(api_url)
        data = response.json()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': 'Internal Server Error'}, status=500)