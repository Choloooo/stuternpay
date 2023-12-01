# users/views.py
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, "index.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back, {}!".format(user.username))
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, "login.html")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        fname = request.POST.get('fullname')
        email = request.POST.get('emailaddress')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Validate username
        try:
            User._meta.get_field('username').run_validators(uname)
        except ValidationError as e:
            messages.error(request, f"Invalid username: {e}")
            return render(request, 'register.html')

        # Validate password
        try:
            validate_password(pass1, User)
        except ValidationError as e:
            messages.error(request, f"Invalid password: {', '.join(e)}")
            return render(request, 'register.html')

        # Check if the passwords match
        if pass1 != pass2:
            messages.error(request, "Your Passwords do not match")
            return render(request, 'register.html')

        try:
            # Create the user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "User has been created successfully. Please log in.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')

    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(
        "index.html"
    )  # Redirect to your home page or any other desired page


def dashboard(request):
    return render(request, "dashboard.html")
