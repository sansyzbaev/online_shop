# Generated by Django 2.1.7 on 2019-04-08 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190408_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]