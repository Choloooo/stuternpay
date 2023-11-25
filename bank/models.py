# models.py

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator


class BankAccount(models.Model):
    account_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255, default="Access bank")
    account_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r"^[0-9]{10}$", "Enter a 10-digit numeric value.")],
    )

    def __str__(self):
        return f"{self.account_name} - {self.account_number}"


class Reason(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
