from django.shortcuts import render
# Create your views here.

def SkinTreatmentAPI(request):
    user=request.user
    return render(request, 'skin_treatment.html',{"user":user})