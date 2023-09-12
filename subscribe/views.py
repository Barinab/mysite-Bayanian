from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from . import models
from subscribe.models import Subscribe

# Create your views here.




def subscribe(request):
    if request.POST:
        email=request.POST['email']
        firstName=request.POST['firstname']
        lastName=request.POST['lastname']

        print("post")
        
        subscribe=Subscribe(first_name=firstName,last_name=lastName,email=email)
        subscribe.save()
    context={}
    return render(request,"subscribe/subscribe.html",context)