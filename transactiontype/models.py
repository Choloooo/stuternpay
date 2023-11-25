# models.py

from django.db import models


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("personal", "Personal"),
        ("business", "Business"),
    ]

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    # Add other fields for your transaction model as needed
