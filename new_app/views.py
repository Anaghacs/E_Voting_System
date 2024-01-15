from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
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

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('base')
        if password !=confirm_password:
            messages.error(request,"Password didn't match !")
            return redirect('base')

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

        user=auth.authenticate(request,username=username,password=pass1)

        if user is not None:

            auth.login(request,user)

            if user.is_superuser:
                return render(request,'admin_home.html')
            else:
                # if user.is_staff==True:
                    return render(request,'user_home.html')
                # else:
                    # messages.error(request,"Your account not approved! Please wait an see!")
        else:
            messages.error(request,"Invalid login credentials")
            return redirect('login')
        
    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect("index")

def admin_home(request):
    return render(request,'admin_home.html')

def user_login(request):
    return render(request,"user_home.html")

def user_home(request):
    return render(request,'user_home.html')

def view_users(request):
    user=User.objects.filter(is_staff=False)
    return render(request,'view_users.html',{'user':user})

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect("view_users")

def update(request,id):
    user=User.objects.get(id=id)
    return render(request,'update.html',{'user':user})

def approve(request,id):
    user=User.objects.get(id=id)
    user.is_staff=True
    user.save()
    return redirect("verified_users")

def verified_users(request):
    user=User.objects.filter(is_staff=True,is_superuser=False)
    return render(request,'verified_users.html',{'user':user})

def user_view_user(request,id):
    user=User.objects.get(id=id)
    return render(request,'user_view_users.html',{'user':user})

# def candidate_form(request):

