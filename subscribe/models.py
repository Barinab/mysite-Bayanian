from django.db import models

# Create your models here.

class Subscribe(models.Model):
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    matn_email=models.CharField(max_length=1000,null=True)
