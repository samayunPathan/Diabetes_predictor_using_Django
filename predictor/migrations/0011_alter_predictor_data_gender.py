# Generated by Django 4.2.4 on 2023-08-25 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0010_alter_predictor_data_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictor_data',
            name='Gender',
            field=models.PositiveBigIntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True),
        ),
    ]