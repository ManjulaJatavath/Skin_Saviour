from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def SkinTreatmentAPI(request):
    user=request.user
    return render(request, 'skin_treatment.html',{"user":user})