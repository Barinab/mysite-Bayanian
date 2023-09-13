from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from . import models
from subscribe.models import Subscribe
from subscribe.forms import SubscribeFrom

# Create your views here.




def subscribe(request):
    subscribe_form=SubscribeFrom()
    if request.POST:
        subscribe_form=SubscribeFrom(request.POST)
        if subscribe_form.is_valid():
            print("valid")
            
            email=subscribe_form.cleaned_data["email"]
            firstName=subscribe_form.cleaned_data["first_name"]
            lastname=subscribe_form.cleaned_data["last_name"]
            matn_email=subscribe_form.cleaned_data["matn"]
            subscribe=Subscribe(first_name=firstName,last_name=lastname,email=email,matn=matn_email)
            subscribe.save()
            context={}
            return render(request,"subscribe/tanx.html",context)


        print("post")
        
        
    context={"form":subscribe_form}
    return render(request,"subscribe/subscribe.html",context)