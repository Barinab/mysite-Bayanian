from django.db import models

# Create your models here.

class Exp(models.Model):
    Exp_nameCo=models.CharField(max_length=30)
    Exp_date_start=models.CharField(max_length=30)
    Exp_date_finish=models.CharField(max_length=30)
    Exp_title=models.CharField(max_length=60)
    Exp_des=models.CharField(max_length=600)
    
class Edu(models.Model):    
    Edu_nameUni=models.CharField(max_length=30)
    Edu_datestart=models.CharField(max_length=30)
    Edu_datefinish=models.CharField(max_length=30)
    Edu_majarName=models.CharField(max_length=60)
    Edu_des=models.CharField(max_length=600)
    
    
class Pro(models.Model):    
    Pro_name=models.CharField(max_length=30)
    Pro_Coname=models.CharField(max_length=30)
    Pro_date=models.CharField(max_length=30)
    Pro_Subject=models.CharField(max_length=200)
    Pro_des=models.CharField(max_length=600)

class Service(models.Model):    
    Service_name=models.CharField(max_length=30)
    Service_Coname=models.CharField(max_length=30)
    Service_date=models.CharField(max_length=30)
    Service_Subject=models.CharField(max_length=200)
    Service_des=models.CharField(max_length=600)

