# Generated by Django 2.2.6 on 2019-10-09 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccsbadmin', '0002_auto_20191009_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('READ', 'Read'), ('UNREAD', 'Unread'), ('TRASH', 'Trash')], default='UNREAD', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 9, 16, 8, 20, 505675)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 9, 16, 8, 20, 505675)),
        ),
        migrations.AlterField(
            model_name='getintouch',
            name='status',
            field=models.CharField(blank=True, choices=[('READ', 'Read'), ('UNREAD', 'Unread'), ('TRASH', 'Trash')], default='UNREAD', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 9, 16, 8, 20, 510223)),
        ),
    ]