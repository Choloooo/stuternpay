# users/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as auth_login


def home(request):
    return render(request, "index.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, "dashboard.html", {"username": username})
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = request.POST
        username = form["username"]
        firstname = form["firstname"]
        email = form["email"]
        lastname = form["lastname"]
        password1 = form["password"]
        password2 = form["confirmpassword"]

        myuser = User.objects.create_user(username, email, password1)
        myuser.firstname = firstname
        myuser.lastname = lastname

        myuser.save()
        messages.success(request, "your account has been successfully created")
        return redirect("login")

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Change 'home' to the URL of your home page
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(
        "index.html"
    )  # Redirect to your home page or any other desired page


def dashboard(request):
    return render(request, "dashboard.html")
