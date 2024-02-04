# myapp/urls.py
from django.urls import path
from .views import register, home, sign_in, logout, dashboard, sign_out

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", sign_in, name="login"),
   
    path("dashboard/", dashboard, name="dashboard"),
    path("", home, name="home"),
    path('signout/', sign_out, name='signout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
