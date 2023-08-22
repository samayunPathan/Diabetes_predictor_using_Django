from django.shortcuts import render
from django.http import HttpResponse
from predictor import forms

# Create your views here.

# def form(request):
#     user_form=forms.UserForm()
#     diction={'user_form':user_form}
#     return render(request,'predictor/index.html',context=diction)
def home(request):
    new_form=forms.UserForm()
    diction={'key':new_form}
    return render(request,'predictor/index.html',context=diction)
def form(request):
    data_form=forms.DataForm()
    diction={'key':data_form}
    return render(request,'predictor/form.html',context=diction)
