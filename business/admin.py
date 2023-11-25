# forms.py

from django import forms
from .models import Business


class BusinessRegistrationForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            "name",
            "rc_number",
            "cac_number",
            "cac_certificate",
            "nature_of_business",
        ]
