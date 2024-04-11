from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
