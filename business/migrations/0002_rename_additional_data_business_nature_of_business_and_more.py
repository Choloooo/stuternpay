# Generated by Django 4.2.7 on 2023-11-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='additional_data',
            new_name='nature_of_business',
        ),
        migrations.AddField(
            model_name='business',
            name='cac_certificate',
            field=models.FileField(blank=True, null=True, upload_to='cac_certificates/'),
        ),
        migrations.AddField(
            model_name='business',
            name='cac_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]