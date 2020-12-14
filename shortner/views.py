from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import User,SiteAnnouncement,Url
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.core.mail import send_mail
import secrets

# Create your views here.
def home(request):
    announcement = SiteAnnouncement.objects.all()
    return render(request,'home.html',{'announcement':announcement})

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        User.objects.create_user(username=username,password=password,first_name=first_name,email=email)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Registration Success')
        return redirect('/')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid - Url')
        return redirect('/')

def redirector(request,id):
    try:    
        obj=Url.objects.get(shorter_name=id)
        print(obj.visitor)
        obj.visitor = obj.visitor+1
        obj.save()
        return HttpResponseRedirect(obj.original_link)
    except Exception as e:
        return render(request,'wrong.html')

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        obj = authenticate(username=username,password=password)
        if obj is not None:
            auth.login(request,obj)
            storage = messages.get_messages(request)
            storage.used = True
            messages.info(request,'Login Success')
            return redirect('/dashboard')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Invalid - Url')
        return redirect('/')

def logout(request):
    auth.logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.info(request,'Logout Successful')
    return redirect('/')

def dashboard(request):
    return render(request,'dashboard.html')

def addlink(request):
    if request.method=="POST":
        shortner_name=request.POST['shortner_link']
        if shortner_name=="":
            shortner_name=secrets.token_hex(5)  
        original_link=request.POST["original_link"]
        Url.objects.create(shorter_name=shortner_name,original_link=original_link,created_by=request.user)
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Link Created. Check it at 127.0.0.1:8000/link/'+shortner_name)
        return redirect('/dashboard')
    else:
        return render(request,'addlink.html')

def mylink(request):
    obj = Url.objects.filter(created_by=request.user)
    return render(request,'mylink.html',{'obj':obj})