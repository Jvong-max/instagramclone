# Generated by Django 3.1.2 on 2020-12-16 21:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0024_auto_20201216_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='DislikeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dislikes', models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
