# Generated by Django 4.2.9 on 2024-02-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0008_customer_group_customer_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="group",
            field=models.IntegerField(default=2),
        ),
    ]
