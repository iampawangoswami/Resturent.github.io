# Generated by Django 2.2.4 on 2019-08-31 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 31, 8, 27, 21, 66416)),
        ),
        migrations.AlterField(
            model_name='dish',
            name='isVeg',
            field=models.BooleanField(default=True),
        ),
    ]
