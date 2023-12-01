from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Payment(models.Model):
    PAYMENT_CHOICES = [
        ("transfer", "Pay with Transfer"),
        ("card", "Pay with Card"),
    ]

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    def __str__(self):
        return self.get_payment_method_display()


class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beneficiaryAccountNumber = models.CharField(max_length=255)
    toCurrency = models.CharField(max_length=255)
    sendAmount = models.DecimalField(max_digits=10, decimal_places=2)
    beneficiaryName = models.CharField(max_length=255)
    bankName = models.CharField(max_length=255)
    swift = models.CharField(max_length=255)
    totalAmountWithFee = models.DecimalField(max_digits=10, decimal_places=2)
    iban = models.CharField(max_length=255)
    feeAmount = models.DecimalField(max_digits=10, decimal_places=2)
    fromCurrency = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    recipientAmount = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment Transaction {self.pk} by {self.user.username}"
