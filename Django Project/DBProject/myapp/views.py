from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':
        newdata=studform(request.POST)
        if newdata.is_valid():
            newdata.save()
            print("Your data saved!")
        else:
            print(newdata.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})