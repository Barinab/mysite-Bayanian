
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Edu_show, name="home"),
    
]