# forms.py

from django import forms
from .models import Beneficiary


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ["name", "account_number"]  # Add other fields as needed
