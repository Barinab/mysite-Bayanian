from django.db import models


# Create your models here.

class Exp(models.Model):
    def __str__(self) -> str:
        return self.Exp_nameCo,self.Exp_date_start,self.Exp_date_finish,self.Exp_title,self.Exp_des
    
    Exp_nameCo=models.CharField(max_length=30,null=True)
    Exp_date_start=models.CharField(max_length=30,null=True)
    Exp_date_finish=models.CharField(max_length=30,null=True)
    Exp_title=models.CharField(max_length=60,null=True)
    Exp_des=models.CharField(max_length=600,null=True)
    slug=models.SlugField(null=True)
    
class Edu(models.Model):  
    def __str__(self):
        return self.Edu_nameUni, self.Edu_datestart,self.Edu_datefinish,self.Edu_des,self.Edu_majarName
    Edu_nameUni=models.CharField(max_length=50)
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
    
    

