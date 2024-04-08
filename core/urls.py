from django.urls import path, include
from .views import AuthView, result
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

urlpatterns = [
    path("", result, name='result'),
    path("signup/", AuthView, name='authview'),
    path("accounts/", include("django.contrib.auth.urls")),
]
