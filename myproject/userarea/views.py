from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(req):
    if req.method == "POST":
        name = req.POST["name"]
        email = req.POST["email"]
        password = req.POST["password"]
        confirmpassword = req.POST["confirmpassword"]

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.info(req, "Email already exists")
            else:
                # create user
                user = User.objects.create(
                    name = name,
                    email = email,
                    password = password,
                )  

                user.save()
                return redirect("login")
        return render(req, "register.html")
            
    return render(req, "register.html")


def login(req):
    if req.method == "POSt":
        email = req.POST["email"]
        password = req.POST["password"]

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect("dashboard")
        else:
            messages.info(req, "Invalid Credentials")

    return render(req, "login.html")



def dashboard(req):
    if not req.user.is_authenticated:
        messages.info(req, "You Have to Login")
        return redirect("login") 
        
    return render(req, "dashboard.html")