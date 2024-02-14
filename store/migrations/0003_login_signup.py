# Generated by Django 5.0.1 on 2024-02-02 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_is_sale_product_sale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=40)),
                ('Lname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], default='m', help_text='Select Gender below', max_length=6)),
                ('user_type', models.CharField(blank=True, choices=[('f', 'Farmer'), ('v', 'Vendor')], default='f', help_text='Select Role below', max_length=6)),
            ],
        ),
    ]
