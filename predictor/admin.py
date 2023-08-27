from django.contrib import admin
from predictor import models


# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display=('User_Name','User_Age','Gender','predictions')

admin.site.register(models.predictor_data,DataAdmin)
