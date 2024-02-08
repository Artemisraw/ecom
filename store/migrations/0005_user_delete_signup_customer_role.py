# Generated by Django 4.2.7 on 2024-02-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_password1_login_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=40)),
                ('lName', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], default='m', help_text='Select Gender below', max_length=6)),
                ('user_type', models.CharField(blank=True, choices=[('f', 'Farmer'), ('v', 'Vendor')], default='Farmer', help_text='Select Role below', max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.CharField(default='f', max_length=50),
            preserve_default=False,
        ),
    ]
