from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


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

        return redirect('login')
    return render(request,'signup.html')

def signin(request):

    return
    render(request,'base.html')

def login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password1']

        user=authenticate(username=username,pasword=pass1)

        if user is not None:
            login(request,user)

        else:
            messages.error(request,"Bad Credential")
            fname=user.first_name
            return redirect(request,'admin_home.html',{'fname':fname})
    
    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect("base")

def admin_home(request):
    return render(request,'admin_home.html')

def view_users(request):
    user=User.objects.filter(is_staff=False)
    return render(request,'view_users.html',{'user':user})

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect("view_users")
