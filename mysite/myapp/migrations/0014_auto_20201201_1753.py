# Generated by Django 3.1.2 on 2020-12-01 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20201201_1731'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]