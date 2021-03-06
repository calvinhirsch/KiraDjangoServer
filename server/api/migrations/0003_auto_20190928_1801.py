# Generated by Django 2.2.5 on 2019-09-28 18:01

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190928_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duedate',
            name='id',
        ),
        migrations.RemoveField(
            model_name='enrolleduser',
            name='id',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='id',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='submittedphoto',
            name='photouid',
        ),
        migrations.RemoveField(
            model_name='trial',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trial',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='usertrial',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usertrial',
            name='uid',
        ),
        migrations.AddField(
            model_name='duedate',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enrolleduser',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, db_column='_id', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submittedphoto',
            name='photoId',
            field=models.CharField(default=1, max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trial',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertrial',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='enrolleduser',
            name='uid',
            field=models.CharField(max_length=24),
        ),
    ]
