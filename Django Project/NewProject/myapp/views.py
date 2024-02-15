from django.shortcuts import render
import random

# Create your views here.
n=1
def index(request):
    name='Prasiddh'
    num=random.randint(1111,9999)
    return render(request,'index.html',{'nm':name,'num':num})

def about(request):
    global n
    n+=1
    return render(request,'about.html',{'n':n})

def contact(request):
    return render(request,'contact.html')