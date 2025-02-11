# Generated by Django 3.1.1 on 2020-09-30 03:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_favorites_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone number')),
                ('company_name', models.CharField(max_length=50, verbose_name='comapny name')),
                ('address1', models.CharField(max_length=400, verbose_name='address line 01')),
                ('address2', models.CharField(max_length=400, verbose_name='address line 02')),
                ('country', models.CharField(max_length=50, verbose_name='country')),
                ('town', models.CharField(max_length=80, verbose_name='town')),
                ('district', models.CharField(max_length=80, verbose_name='district')),
                ('postcode', models.IntegerField(null=True, verbose_name='postcode/zipcode')),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
            ],
        ),
    ]
