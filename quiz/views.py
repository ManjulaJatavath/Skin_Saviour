from django.shortcuts import render
from rest_framework import status
from quiz.models import QuizModel
# Create your views here.

def QuizAPI(request):
    return render(request, 'quiz.html')

def save_data(request):
    if request.method == 'POST':
        treatment = request.POST.get('treatment')
        age = request.POST.get('age')
        skin_type = request.POST.get('skin_type')
        skin_concerns = ','.join(request.POST.getlist('skin_concerns'))
        react_to_new_products = request.POST.get('react_to_new_products')
        sensitive = request.POST.get('sensitive')
        sleep_cycle = request.POST.get('sleep_cycle')
        skincare_texture = request.POST.get('skincare_texture')
        
        quiz_model= QuizModel(
            treatment=treatment,
            age=age,
            skin_type=skin_type,
            skin_concerns=skin_concerns,
            react_to_new_products=react_to_new_products,
            sensitive=sensitive,
            sleep_cycle=sleep_cycle,
            skincare_texture=skincare_texture
        )
        quiz_model.save()
        return render(request, 'quiz.html')
    return render(request, 'home.html')
