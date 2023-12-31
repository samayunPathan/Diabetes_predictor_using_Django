# Generated by Django 4.2.4 on 2023-08-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0006_predictor_data_polydipsia_predictor_data_polyphagia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictor_data',
            name='Polydipsia',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='predictor_data',
            name='Polyphagia',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='predictor_data',
            name='Polyuria',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='predictor_data',
            name='partial_paresis',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='predictor_data',
            name='sudden_weight_loss',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='predictor_data',
            name='weakness',
            field=models.PositiveBigIntegerField(choices=[(1, 'Yes'), (2, 'No')], null=True),
        ),
    ]
