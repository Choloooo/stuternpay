# users/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, "index.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Welcome back, {}!".format(user.username))
            return redirect("dashboard")  # Replace 'dashboard' with the actual URL name
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password"]
            password2 = form.cleaned_data["confirmpassword"]

            # Check if passwords match
            if password1 != password2:
                messages.error(request, "Passwords do not match")
                return render(request, "register.html", {"form": form})

            # Additional validation for weak password
            if len(password1) < 8:
                messages.error(request, "Password must be at least 8 characters long")
                return render(request, "register.html", {"form": form})

            # Check if username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return render(request, "register.html", {"form": form})

            # Check if email is already in use
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already in use")
                return render(request, "register.html", {"form": form})

            # Create the user
            user = User.objects.create_user(username, email, password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            # Log in the user
            auth_login(request, user)

            messages.success(request, "Your account has been successfully created")
            return redirect("login")  # Change 'login' to the URL of your login page
        else:
            # Form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

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
