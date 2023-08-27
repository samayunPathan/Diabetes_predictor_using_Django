# Generated by Django 4.2.4 on 2023-08-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0008_predictor_data_gender_predictor_data_obesity_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='predictor_data',
            name='User_Age',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='predictor_data',
            name='User_Name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]