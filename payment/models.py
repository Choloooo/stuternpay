from django.db import models


# Create your models here.
class Payment(models.Model):
    PAYMENT_CHOICES = [
        ("transfer", "Pay with Transfer"),
        ("card", "Pay with Card"),
    ]

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    def __str__(self):
        return self.get_payment_method_display()
