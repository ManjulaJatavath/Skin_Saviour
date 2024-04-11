import time
from django.db import IntegrityError
from django.shortcuts import render,redirect
from rest_framework import status
from quiz.models import QuizModel
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def QuizAPI(request):
    user=request.user
    
    data=QuizModel.objects.filter(user=user)
    if(data):
        data1=data.latest('id')
        context={
            "user":data1.user,
            "treatment":data1.treatment,
            "age":data1.age,
            "skin_type":data1.skin_type
        }
        return render(request, 'quiz.html',{"context":context})
    return render(request, 'quiz.html')

def save_data(request):
    if request.method == 'POST':
        user = request.user
        treatment = request.POST.get('treatment')
        age = request.POST.get('age')
        skin_type = request.POST.get('skin_type')
        skin_concerns = ','.join(request.POST.getlist('skin_concerns'))
        react_to_new_products = request.POST.get('react_to_new_products')
        sensitive = request.POST.get('sensitive')
        sleep_cycle = request.POST.get('sleep_cycle')
        skincare_texture = request.POST.get('skincare_texture')
        
        quiz_data= QuizModel(
            user=user,
            treatment=treatment,
            age=age,
            skin_type=skin_type,
            skin_concerns=skin_concerns,
            react_to_new_products=react_to_new_products,
            sensitive=sensitive,
            sleep_cycle=sleep_cycle,
            skincare_texture=skincare_texture
        )
        quiz_data.save()
        time.sleep(5)
        return redirect('quiz')

    return render(request, 'quiz.html')
