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
            username=usersignup.objects.get(username=unm)
            print("Username:",username.id)
            if user: #TRUE
                print("Login Successfull!")
                request.session['user']=unm
                request.session['userid']=username.id
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
    user=request.session.get('user')
    userid=request.session.get('userid')
    cuser=usersignup.objects.get(id=userid)
    if request.method=='POST':
            newuser=signupForm(request.POST,instance=cuser)
            if newuser.is_valid():
                newuser.save()
                print("Update Successfully!")
                msg="Update Successfully!"
                return redirect('notes')
            else:
                print(newuser.errors)
                msg="Error!Something went wrong...Try again"
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

