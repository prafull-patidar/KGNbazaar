# Generated by Django 3.1.1 on 2020-09-30 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_auto_20200930_0347'),
        ('Store', '0003_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user_profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='useraccount.userprofile'),
            preserve_default=False,
        ),
    ]
