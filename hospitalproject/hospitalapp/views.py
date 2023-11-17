from django.contrib import messages, auth
from django.template import loader
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from.models import Medicine
from.models import Doctors



def new3(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def doctors(request):
    obj1=Doctors.objects.all()
    context={'results':obj1}
    return render(request, "doctors.html",context)
    
def departments(request):
    return render(request,"departments.html")
def medicine(request):
    obj=Medicine.objects.all()
    context={'result':obj}
    return render(request, "medicine.html",context)
   
def contact(request):
    return render(request,"contact.html")
def booking(request):
    # if request.method=="POST":
    #     form=booking(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"register.html")
    # else:
    #     form=booking()
    # dict_form={
    #     'form':form
    # }
    return render(request,"booking.html")
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect ("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect ("register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)


                user.save()
                return redirect('login')
            
        else:
            messages.info(request,"password not matching")
            return redirect("register")

        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

