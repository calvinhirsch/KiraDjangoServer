# Generated by Django 2.2.5 on 2019-09-29 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_trial_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrial',
            name='trialId',
            field=models.CharField(default=1, max_length=24),
            preserve_default=False,
        ),
    ]