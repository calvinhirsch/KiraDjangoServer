# Generated by Django 2.2.5 on 2019-09-28 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='valuid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='folders',
        ),
    ]
