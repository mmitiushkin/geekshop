# Generated by Django 3.2.8 on 2021-11-15 18:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211111_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 18, 25, 56, 441848, tzinfo=utc)),
        ),
    ]
