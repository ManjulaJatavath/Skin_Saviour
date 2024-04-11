"""
URL configuration for SkinSaviour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import HomeAPI
from about.views import AboutAPI
from quiz.views import QuizAPI
from contact_us.views import ContactUsAPI
from skin_treatment.views import SkinTreatmentAPI
from tips.views import TipsAPI
from core.views import AuthView,LoginAPI,Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), 'core')),
    path('home/',HomeAPI,name="home"),
    path('about/',AboutAPI,name="about"),
    path('quiz/',QuizAPI,name="quiz"),
    path('contact_us/',ContactUsAPI,name="contact_us"),
    path('skin_treatment/',SkinTreatmentAPI,name="skin_treatment"),
    path('tips/',TipsAPI,name="tips"),
    path('login/',LoginAPI,name="login"),
    path('signup/',AuthView,name="signup"),
    path('logout/',Logout,name="logout")
]
