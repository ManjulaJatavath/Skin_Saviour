from django.shortcuts import render
# Create your views here.

def RegisterAPI(request):
    return render(request, 'register.html')