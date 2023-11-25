# myapp/urls.py
from django.urls import path
from .views import register, home, sign_in, logout, dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", sign_in, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("", home, name="home"),
]
