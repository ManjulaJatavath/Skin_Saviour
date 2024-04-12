from django.shortcuts import render

from quiz.models import QuizModel
from skin_treatment.models.face_wash import FaceWashModel
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def SkinTreatmentAPI(request):
       user=request.user
       data = QuizModel.objects.get(user=user)
       if data:
               data = QuizModel.objects.latest('id')
               suggested_facewash = FaceWashModel.objects.filter(
                    treatment__treatment=data.treatment,
                    age__age=data.age,
                    skin_type__skin_type=data.skin_type,
                    skin_concern__skin_concern=data.skin_concerns,
                    react_to_new_products__react_to_new_products=data.react_to_new_products,
                    senstive__senstive=data.sensitive,
                    sleep_cycle__sleep_cycle=data.sleep_cycle,
                    skincare_texture__skin_texture=data.skincare_texture
                        )
               print(suggested_facewash)
               return render(request, 'skin_treatment.html', {'suggested_facewash': list(suggested_facewash)}) 
       return render(request, 'skin_treatment.html',{"user":user})  

