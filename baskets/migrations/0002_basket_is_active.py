# Generated by Django 3.2.8 on 2021-12-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
