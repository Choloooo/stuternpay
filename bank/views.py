# views.py

from django.shortcuts import render
from .models import BankAccount, Reason


def get_account_details(request):
    static_account = (
        BankAccount.objects.first()
    )  # Assuming you have only one static account
    return render(request, "account_details.html", {"account": static_account})


def list_of_reason(request):
    # Create instances of the Reason model
    # Reason.objects.create(name="Reason 1")
    # Reason.objects.create(name="Reason 2")
    # ... add more instances as needed

    # Retrieve all reasons from the database
    reasons = Reason.objects.all()

    return render(request, "personalsend.html", {"reasons": reasons})
