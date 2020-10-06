# Generated by Django 3.1.1 on 2020-10-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0015_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
    ]
