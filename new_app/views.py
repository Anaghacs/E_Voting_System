from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return render(request,'base.html')

def signup(request):

    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_id=request.POST['email']
        password=request.POST['password1']
        confirm_password=request.POST['password2']

        my_user=User.objects.create_user(username,email_id,password)
        my_user.first_name=first_name
        my_user.last_name=last_name

        my_user.save()

        messages.success(request,"Your Account has been successfully created")

        # status=['status']

        return redirect('login')

    return render(request,'signup.html')

def signin(request):

    return render(request,'signin.html')

def signin(request):

    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password1']

        user=authenticate(username=username,pasword=pass1)

        if user is not None:
            login(request,user)


    return render(request,'login.html')

def signout(request):
    pass
    # return render(request,'signo.html')