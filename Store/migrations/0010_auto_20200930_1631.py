# Generated by Django 3.1.1 on 2020-09-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_auto_20200930_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdates',
            name='update_timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
