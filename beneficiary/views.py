# views.py
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Beneficiary
from django.http import HttpResponse, JsonResponse


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
@login_required
def add_beneficiary(request):
    if request.method == 'POST':
        data = request.POST  # Use request.POST to access form data

        print(data)  # Add this line to print form data for debugging

        beneficiary = Beneficiary(
            user=request.user,  # Adjust based on your authentication
            name=data.get('beneficiaryName'),
            account_number=data.get('beneficiaryAccountNumber'),
            bank_name=data.get('bankName'),
            country=data.get('country'),
            swift_code=data.get('swift'),
            iban=data.get('iban'),
            # Add other fields as needed
        )
        beneficiary.save()
        return redirect('payment_confirmation')

        return JsonResponse({'message': 'Beneficiary details saved successfully'})

    # Handle other HTTP methods if needed
    return render(request, 'beneficiary.html')