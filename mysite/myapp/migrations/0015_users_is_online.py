# Generated by Django 5.1.4 on 2024-12-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_inventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="is_online",
            field=models.BooleanField(default=False),
        ),
    ]
