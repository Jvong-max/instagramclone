# Generated by Django 3.1.2 on 2020-12-16 12:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0017_auto_20201216_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestionmodel',
            name='likes',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
