# Generated by Django 4.2.7 on 2023-12-15 10:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0004_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='buyers',
            field=models.ManyToManyField(blank=True, related_name='bought_cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
