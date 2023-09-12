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

        print("post")
        
        
    context={"form":subscribe_form}
    return render(request,"subscribe/subscribe.html",context)