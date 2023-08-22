from django.db import models

# Create your models here.

class User(models.Model):
    User_Name=models.CharField(max_length=30)
    User_Age=models.CharField(max_length=2,null=True)

class predictor_data(models.Model):
    Polyuria=models.CharField(max_length=10)
    Polydipsia =models.CharField(max_length=10)
    sudden_weight_loss=models.CharField(max_length=10)
    weakness=models.CharField(max_length=10)
    Polyphagia =models.CharField(max_length=10)
    partial_paresis=models.CharField(max_length=10)
 