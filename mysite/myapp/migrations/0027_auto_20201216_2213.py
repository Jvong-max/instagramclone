# Generated by Django 3.1.2 on 2020-12-16 22:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0026_suggestionmodel_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestionmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
