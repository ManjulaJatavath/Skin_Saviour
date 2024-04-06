from django.shortcuts import render
# Create your views here.

def QuizAPI(request):
    return render(request, 'quiz.html')
