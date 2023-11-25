# Generated by Django 4.2.7 on 2023-11-24 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('transfer', 'Pay with Transfer'), ('card', 'Pay with Card')], max_length=10)),
            ],
        ),
    ]