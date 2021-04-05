from django.shortcuts import render
from app1 import views

app_name = "app1"

# Create your views here.

def index(request):
    return render(request,"sample1.html")