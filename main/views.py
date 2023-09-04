from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


edu_list=[
    "The University Of Adelaide",
    "the olum"
       
]
edu_majar=["mechatrinics",
           "mechanization"]

def home(request):
    context={}
    return render(request,"main/home.html",context)



def Edu_show(request):
    list_of_Edu="<ul>"
    for j in edu_list:
        list_of_Edu += f"<li>{j}</li>"
    list_of_Edu +="</ul>"
    return HttpResponse(list_of_Edu)


