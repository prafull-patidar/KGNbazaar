# Generated by Django 3.1.1 on 2020-09-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_auto_20200929_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='items_json',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='order_id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
