from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def result(request):
    return render(request, 'home.html', {})

def AuthView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form  = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def RegisterAPI(request):
    return render(request, 'register.html')
