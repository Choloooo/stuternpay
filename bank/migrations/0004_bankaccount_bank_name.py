# Generated by Django 4.2.7 on 2023-11-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_alter_bankaccount_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='bank_name',
            field=models.CharField(default='Access bank', max_length=255),
        ),
    ]
