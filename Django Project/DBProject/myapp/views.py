from django.shortcuts import render,redirect
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

def updatedata(request,id):
    stdata=studinfo.objects.get(id=id)
    if request.method=='POST':
        newdata=studform(request.POST,instance=stdata)
        if newdata.is_valid():
            newdata.save()
            print("Your data updated!")
            return redirect('showdata')
        else:
            print(newdata.errors)
    return render(request,'updatedata.html',{'stdata':stdata})

def deletedata(request,id):
    stdata=studinfo.objects.get(id=id)
    studinfo.delete(stdata)
    return redirect('showdata')
    