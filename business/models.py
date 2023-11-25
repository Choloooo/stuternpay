# models.py

from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    rc_number = models.CharField(max_length=20, unique=True)
    cac_number = models.CharField(max_length=20, blank=True, null=True)
    cac_certificate = models.FileField(
        upload_to="cac_certificates/", blank=True, null=True
    )
    nature_of_business = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
