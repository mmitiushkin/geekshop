# Generated by Django 3.2.8 on 2021-11-26 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 16, 13, 8, 436629, tzinfo=utc)),
        ),
    ]
