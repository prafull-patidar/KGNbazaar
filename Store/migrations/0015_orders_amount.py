# Generated by Django 3.1.1 on 2020-10-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0014_userquerrys'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
