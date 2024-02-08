# Generated by Django 4.2.7 on 2024-02-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_user_delete_signup_customer_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('f', 'Farmer'), ('v', 'Vendor')], default='', help_text='Select Role below', max_length=6),
        ),
    ]
