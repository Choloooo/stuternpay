# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Beneficiary
from django.http import HttpResponse


@login_required
def add_beneficiary(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get("fullname")
        account_number = request.POST.get("accountnumber")
        bank_name = request.POST.get("bankname")
        country = request.POST.get("country")
        swift_code = request.POST.get("swiftcode", "")
        iban = request.POST.get("iban", "")
        address = request.POST.get("address", "")

        # Validate the data if needed
        if name and account_number and bank_name and country:
            # Save the beneficiary to the database
            Beneficiary.objects.create(
                user=user,
                name=name,
                account_number=account_number,
                bank_name=bank_name,
                country=country,
                swift_code=swift_code,
                iban=iban,
                address=address,
            )
            return HttpResponse(
                "Beneficiary added successfully"
            )  # You can redirect or render a success page here

    return render(request, "add_beneficiary.html")
