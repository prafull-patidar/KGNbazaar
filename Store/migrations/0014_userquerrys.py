# Generated by Django 3.1.1 on 2020-10-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_orders_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuerrys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('querry', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
    ]
