# Generated by Django 5.1.4 on 2024-12-25 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_alter_currency_user_alter_transaction_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="currency",
            name="user",
        ),
    ]
