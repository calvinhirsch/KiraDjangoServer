# Generated by Django 2.2.5 on 2019-09-29 07:24

import api.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_usertrial_trialid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisResults',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('actinic_keratoses', models.FloatField()),
                ('basal_cell_carcinoma', models.FloatField()),
                ('benign_keratosis', models.FloatField()),
                ('dermatofibroma', models.FloatField()),
                ('malignant_melanoma', models.FloatField()),
                ('melanocytic_nevi', models.FloatField()),
                ('vascular_lesions', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='analysisResults',
            field=djongo.models.fields.EmbeddedModelField(model_container=api.models.AnalysisResults, null=True),
        ),
    ]
