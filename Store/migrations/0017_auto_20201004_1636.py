# Generated by Django 3.1.1 on 2020-10-04 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store', '0016_auto_20201002_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='country',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='district',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='town',
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='items_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
