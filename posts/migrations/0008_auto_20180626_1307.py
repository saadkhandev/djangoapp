# Generated by Django 2.0.5 on 2018-06-26 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20180626_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 26, 13, 7, 13, 157971)),
        ),
    ]