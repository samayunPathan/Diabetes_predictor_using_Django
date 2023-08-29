from django import forms
from django.core import validators
from predictor import models

class DataForm(forms.ModelForm):
    class Meta:
        model=models.predictor_data
        fields=('User_Name','User_Age','Gender','Polyuria','Polydipsia' ,'sudden_weight_loss','weakness','Polyphagia', 'delayed_healing','partial_paresis','Obesity')
        labels={
            'User_Name':'Name',
            'User_Age':'Age',
            'Gender':'Gender ? ',
            'Polyuria':'Excessive Or An Abnormally Large Production Of Urine ? ',
            'Polydipsia':'Excessive Thirst ? ',
            'sudden_weight_loss':'Sudden Weight Loss ? ',
            'weakness':'Feel Weak ? ',
            'Polyphagia':'Excessive Appetite ? ',
            'delayed_healing':'The Wound Has Trouble Healing Or Staying Closed ? ',
            'partial_paresis':'Weakening Of A Muscle Or Group Of Muscles ? ',
            'Obesity':'Anormal Or Excessive Fat Accumulation ? ',
            
        }