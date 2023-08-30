from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
import joblib

# Create your models here.


class predictor_data(models.Model):
    
    class gender(models.TextChoices):
        m='Male','Male'
        f='Female','Female'
        o= 'LGBTIQA+',' LGBTIQA+'
    
    class makechoise(models.IntegerChoices):
        A = 0, "NO"
        B = 1, "YES"
        

    
    User_Name=models.CharField(max_length=30,null=True)
    User_Age=models.PositiveIntegerField(validators=[MinValueValidator(20),MaxValueValidator(80)],null=True)
    Gender=models.CharField(max_length=20,choices=gender.choices,null=True)
    Polyuria=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Polydipsia =models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    sudden_weight_loss=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    weakness=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Polyphagia =models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Irritability=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    delayed_healing=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    partial_paresis=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    Obesity=models.PositiveBigIntegerField(choices=makechoise.choices,null=True)
    predictions=models.CharField(max_length=20,blank=True)

    def save(self,*args,**kwargs):
        ml_model=joblib.load('ml_model/finalized_model.joblib')
        self.predictions=ml_model.predict([[self.User_Age,self.Polyuria,self.Polydipsia,self.sudden_weight_loss,self.weakness,self.Polyphagia,self.Irritability,self.delayed_healing,self.partial_paresis,self.Obesity]])
        return super().save(*args,**kwargs)


    def __str__(self):
        return self.User_Name
    # +" "+str(self.User_Age)+" "+str(self.Gender)+" "+self.predictions

 