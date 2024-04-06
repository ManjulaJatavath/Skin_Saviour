from django.shortcuts import render
# Create your views here.

def SkinTreatmentAPI(request):
    return render(request, 'skin_treatment.html')