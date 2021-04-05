from django.shortcuts import render

# Create your views here.
from app2 import views

app_name = "app2"

# Create your views here.

def index(request):
    return render(request,"sample1.html")