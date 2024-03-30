from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    msg=""
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
                msg="Signup Successfully!"
            else:
                print(newuser.errors)
                msg="Error!Something went wrong...Try again"
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=usersignup.objects.filter(username=unm,password=pas)
            if user: #TRUE
                print("Login Successfull!")
                request.session['user']=unm
                return redirect('notes')
            else:
                print("Error!Login Faild...")
                msg="Error!Login Faild..."
    return render(request,'index.html',{'msg':msg})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

