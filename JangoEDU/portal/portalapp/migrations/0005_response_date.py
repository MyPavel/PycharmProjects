# Generated by Django 4.0.6 on 2023-02-06 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0004_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
