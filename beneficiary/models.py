from django.db import models
from django.contrib.auth.models import User


class Beneficiary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=20, blank=True, null=True)
    iban = models.CharField(max_length=34, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    # Add other relevant fields for international transactions

    def __str__(self):
        return self.name
