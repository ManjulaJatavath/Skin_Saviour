from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import time
# Create your views here.

def AuthView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form  = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def LoginAPI(request):
    return redirect('skin_treatment')

def Logout(request):
    logout(request)
    time.sleep(3)
    return redirect('home')
