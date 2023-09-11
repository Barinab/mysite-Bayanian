from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from . import models
from main.models import Edu,Exp,Pro,Service

# Create your views here.




def home(request):
    context={}
    return render(request,"main/home.html",context)


def Edu_detail(request, id):
        print(type(id))

        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context={"Edu_nameUni":Edu.Edu_nameUni[id], "job_description":Edu.Edu_nameUni[id]}
        return render(request, "main/home.html", context)
   
    # "<domain>/job/1" --> Job detail page
    
def Edu_show(request):
    '''  list_of_Edu="<ul>"
    for j in edu_list:
        list_of_Edu += f"<li>{j}</li>"
    list_of_Edu +="</ul>"
    '''
    namayesh_daneshga=Edu.objects.all()
    context={"edus":namayesh_daneshga}
    return render(request,"main/home.html",context)



def Edu_tak(request,id):
    namayesh_riz=Edu.objects.get(id=id)
    context={"Edu_nameUni":Edu.Edu_nameUni[id], "job_description":Edu.Edu_nameUni[id]}
    return(request,"main/home.html",context)

