from django.shortcuts import render

from quiz.models import QuizModel
from skin_treatment.models.face_wash import FaceWashModel
from skin_treatment.models.serum import SerumModel
from skin_treatment.models.moisturizer import MoisturizerModel
from skin_treatment.models.sunscreen import SunscreenModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def SkinTreatmentAPI(request):
       user=request.user
       if QuizModel.objects.filter(user=user):
            data = QuizModel.objects.filter(user=user).first()
            if data.treatment=="Conventional Products":
                  if data.skin_concerns== 'Sensitivity and redness' and data.react_to_new_products=='Gets irritated and red easily':
                        data.skin_type='Sensitive'
                  elif data.skin_concerns=='Active Acne':
                        data.skin_concerns='Oil Control'
                        data.react_to_new_products='Adapts Well'
                        data.skincare_texture='Gel'
                        data.skin_type='Oily'
                  elif data.skin_concerns=='Dry Patches' or data.skin_concerns=='Dehydration/ Breakouts' and data.react_to_new_products=='Breaks out':
                        data.skin_concerns='Dehydration/ Breakouts'
                        data.react_to_new_products='Adapts Well'
                        data.skin_type='Dry'
                        data.skincare_texture='Cream'
                  elif data.skin_concerns=='Acne Marks' :
                        data.react_to_new_products='Adapts Well'
                        data.skincare_texture='Light Weight'
                        data.skin_type='Combination(Oily at T junction and Dry at cheeks)'
            suggested_facewash = FaceWashModel.objects.filter(
                treatment__treatment=data.treatment,
                age__age=data.age,
                skin_type__skin_type=data.skin_type,
                skin_concern__skin_concern=data.skin_concerns,
                react_to_new_products__react_to_new_products=data.react_to_new_products,
                skincare_texture__skin_texture=data.skincare_texture,
                    )
            suggested_serum = SerumModel.objects.filter(
                treatment__treatment=data.treatment,
                age__age=data.age,
                skin_type__skin_type=data.skin_type,
                skin_concern__skin_concern=data.skin_concerns,
                react_to_new_products__react_to_new_products=data.react_to_new_products,
                skincare_texture__skin_texture=data.skincare_texture,
                    )
            suggested_moisturizer = MoisturizerModel.objects.filter(
                treatment__treatment=data.treatment,
                age__age=data.age,
                skin_type__skin_type=data.skin_type,
                skin_concern__skin_concern=data.skin_concerns,
                react_to_new_products__react_to_new_products=data.react_to_new_products,
                skincare_texture__skin_texture=data.skincare_texture,
                    )
            suggested_sunscreen = SunscreenModel.objects.filter(
                treatment__treatment=data.treatment,
                age__age=data.age,
                skin_type__skin_type=data.skin_type,
                skin_concern__skin_concern=data.skin_concerns,
                react_to_new_products__react_to_new_products=data.react_to_new_products,
                skincare_texture__skin_texture=data.skincare_texture,
                    )
            if data.treatment=="Conventional Products":
                  if not suggested_facewash :
                        suggested_facewash = FaceWashModel.objects.filter(id=2)
                  if not suggested_serum :
                        suggested_serum = SerumModel.objects.filter(id=2)
                  if not suggested_moisturizer :
                        suggested_moisturizer = MoisturizerModel.objects.filter(id=2)
                  if not suggested_sunscreen :
                        suggested_sunscreen = SunscreenModel.objects.filter(id=2)
            return render(request, 'skin_treatment.html', {'suggested_facewash': suggested_facewash,'active_tab': 'skin_treatment', 'suggested_serum': suggested_serum, 'suggested_moisturizer': suggested_moisturizer, 'suggested_sunscreen': suggested_sunscreen, 'skin_type':data}) 
       return render(request, 'skin_treatment.html',{'active_tab': 'skin_treatment', 'message': 'PLEASE TAKE YOUR QUIZ TO GET YOUR TREATMENT'})  

