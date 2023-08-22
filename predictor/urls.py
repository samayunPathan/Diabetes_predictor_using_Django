from django.urls import re_path as url
from django.urls import path
from predictor import views

urlpatterns=[
    path('',views.home,name='home'),
    path('form/',views.form,name='form')
]