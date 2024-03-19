from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method=='POST':
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submitted!")
        else:
            print(newcontact.errors)
    return render(request,'contact.html')

def furniture(request):
    return render(request,'furniture.html')