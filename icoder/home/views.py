from django.shortcuts import render,redirect
from home.models import Contact
from blog.models import Post,BlogComment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request,"home/home.html")
def contact(request):
    messages.success(request,"welcome to contact")
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        content=request.POST["desc"]
        if len(email)<3 or len(phone)!=10 or len(content)<10:
            messages.error(request,"fill form again")

        else:
            contact=Contact(name=name,email=email,phone=phone,desc=content)
            contact.save()
            messages.success(request,"form fill successfull")
    
    return render(request,"home/contact.html")
def about(request):
    return render(request,"home/about.html")  
def search(request):
    query=request.GET["search"]
    posts_title=Post.objects.filter(title__icontains=query)
    posts_content=Post.objects.filter(content__icontains=query)
    posts=posts_title.union(posts_content)
    context={"posts":posts}
    if len(posts)>0:
        return render(request,"home/search.html",context) 
    else:
        return HttpResponse("no post found")        

def handleSignup(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        # check conditions
        if len(username)>10:
            messages.error(request,"username must be less then 10 characters")
            return redirect("/")   
        if pass1 != pass2:
            messages.error(request,"password didnt match")
            return redirect("/")        
             



        #create user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been created")
        return redirect("/")        

    else:
        return HttpResponse("NOT FOUND")        

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST["loginusername"]
        loginpassword=request.POST["loginpassword"]
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully loggedin")
            return redirect("/")
        else:
            messages.error(request,"invalid credentials")  
            return redirect("/")
    return HttpResponse("fuckoff")



    return render(request,"home/about.html")       
def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out") 
    return redirect("/")


