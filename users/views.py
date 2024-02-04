# users/views.py
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "index.html")


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, "login.html")

    return render(request, "login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        uname = request.POST.get('username')
        fname = request.POST.get('fullname')
        email = request.POST.get('emailaddress')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Collect all validation errors
        validation_errors = []

        # Validate username
        try:
            User._meta.get_field('username').run_validators(uname)
            if User.objects.filter(username=uname).exists():
                validation_errors.append("Username already exists.")
        except ValidationError as e:
            validation_errors.append(f"Invalid username: {e.messages[0]}" if e.messages else "Unknown error")

        # Validate password
        try:
            validate_password(pass1, User)
        except ValidationError as e:
            validation_errors.append(f"Invalid password: {', '.join(map(str, e))}")

        # Check if the passwords match
        if pass1 != pass2:
            validation_errors.append("Password mismatch: Your passwords do not match.")

        # If there are validation errors, display them
        if validation_errors:
            for error in validation_errors:
                messages.error(request, error)
            return render(request, 'register.html')

        try:
            # Create the user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.full_name = fname
            my_user.save()
            messages.success(request, "User has been created successfully. Please log in.")
            return redirect("login")
        except IntegrityError:
            messages.error(request, "Username or email is already in use.")
            return render(request, 'register.html')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')

    return render(request, "register.html", {"form": form})


def sign_out(request):
    logout(request)

    return redirect(
        "home"
    )  # Redirect to your home page or any other desired page

@login_required(login_url='login')
def dashboard(request):
    return render(request, "dashboard.html")
