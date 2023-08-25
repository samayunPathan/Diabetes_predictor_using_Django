from django.db import models
import joblib

# Create your models here.


class predictor_data(models.Model):
    class Month(models.IntegerChoices):
        JAN = 1, "Yes"
        FEB = 2, "No"
    class gender(models.IntegerChoices):
        m=1,'Male'
        f=2,'Female'
    
    class makechoise(models.IntegerChoices):
        JAN = 0, "YES"
        FEB = 1, "NO"
        

    
    User_Name=models.CharField(max_length=30,null=True)
    User_Age=models.IntegerField(null=True)
    Gender=models.PositiveBigIntegerField(choices=gender.choices,null=True)
    Polyuria=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Polydipsia =models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    sudden_weight_loss=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    weakness=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Polyphagia =models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    delayed_healing=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    partial_paresis=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Obesity=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    predictions=models.CharField(max_length=20,blank=True)

    def save(self,*args,**kwargs):
        ml_model=joblib.load('ml_model/finalized_model.joblib')
        self.predictions=ml_model.predict([[self.Polyuria,self.Polydipsia,self.sudden_weight_loss,self.weakness,self.Polyphagia,self.partial_paresis]])
        return super().save(*args,**kwargs)


    def __str__(self):
        return self.User_Name

 