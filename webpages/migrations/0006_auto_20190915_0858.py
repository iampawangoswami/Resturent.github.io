# Generated by Django 2.2.4 on 2019-09-15 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_auto_20190915_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.TextField()),
                ('mobile', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='dish',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 8, 58, 38, 265904)),
        ),
    ]