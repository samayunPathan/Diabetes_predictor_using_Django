# Generated by Django 4.2.4 on 2023-08-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0007_alter_predictor_data_polydipsia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictor_data',
            name='Gender',
            field=models.PositiveBigIntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
        migrations.AddField(
            model_name='predictor_data',
            name='Obesity',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='predictor_data',
            name='delayed_healing',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
    ]
