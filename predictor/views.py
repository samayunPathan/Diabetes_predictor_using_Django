from django.shortcuts import render
from django.http import HttpResponse
from predictor import forms
from .models import predictor_data
import joblib
# Create your views here.


def home(request):
    diction={'key':'hello Are You want to test diabetes'}
    return render(request,'predictor/index.html',context=diction)
def form(request):
    data_form=forms.DataForm()
    diction={'key':data_form}
    if request.method=='POST':
        data_form=forms.DataForm(request.POST)
        if data_form.is_valid():
            data_form.save(commit=True)
            return result(request)
    return render(request,'predictor/form.html',context=diction)



def result(request):
    predicted = predictor_data.objects.filter().last()
    context = {
        'predicted': predicted
    }
    
    return render(request,'predictor/result.html',context)