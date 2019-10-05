# Generated by Django 2.2.6 on 2019-10-05 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccsbadmin', '0002_auto_20191005_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('UNREAD', 'Unread'), ('READ', 'Read'), ('TRASH', 'Trash')], default='UNREAD', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 5, 12, 40, 26, 130376)),
        ),
        migrations.AlterField(
            model_name='objective',
            name='objective_title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 5, 12, 40, 26, 134366)),
        ),
    ]