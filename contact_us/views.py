from django.shortcuts import render
# Create your views here.

def ContactUsAPI(request):
    return render(request, 'contact_us.html')
