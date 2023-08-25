from django.shortcuts import render
from django.http import HttpResponse
from predictor import forms
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
    # cls=joblib.load('finalized_model.sav')

    # lis=[]
    # # lis.append(request.GET['User_Age'])
    # # lis.append(request.GET['Gender'])
    # lis.append(request.POST.get('Polyuria'))
    # lis.append(request.POST.get('Polydipsia'))
    # lis.append(request.POST.get('udden_weight_loss'))
    # lis.append(request.POST.get('weakness'))
    # lis.append(request.POST.get('Polyphagia'))
    # # lis.append(request.GET['delayed_healing'])
    # lis.append(request.POST.get('partial_paresis'))
    # # lis.append(request.GET['Obesity'])

    # ans=cls.predict([lis])


    diction={}
    return render(request,'predictor/output.html',{'answer':ans})