# Generated by Django 4.2.4 on 2023-08-22 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='Date_of_Birth',
        ),
    ]
