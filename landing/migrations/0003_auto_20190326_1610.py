# Generated by Django 2.1.7 on 2019-03-26 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20190326_1446'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]