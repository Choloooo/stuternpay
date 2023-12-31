# Generated by Django 4.2.7 on 2023-12-01 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaryAccountNumber', models.CharField(max_length=255)),
                ('toCurrency', models.CharField(max_length=255)),
                ('sendAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beneficiaryName', models.CharField(max_length=255)),
                ('bankName', models.CharField(max_length=255)),
                ('swift', models.CharField(max_length=255)),
                ('totalAmountWithFee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iban', models.CharField(max_length=255)),
                ('feeAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fromCurrency', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('recipientAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
