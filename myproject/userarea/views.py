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
            if User.objects.filter(email):
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
            
    return render(req, "regsiter.html")