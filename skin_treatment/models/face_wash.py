from django.db import models
from skin_treatment.models.treatment import *
from utils.helpers.timestamp_model import TimeStampedModel
from utils.helpers.image_file_path import facewash_image

class FaceWashModel(TimeStampedModel):
    treatment = models.ForeignKey(TreatmentModel, on_delete=models.CASCADE)
    age = models.ForeignKey(AgeModel, on_delete=models.CASCADE)
    skin_type = models.ForeignKey(SkinTypeModel, on_delete=models.CASCADE)
    skin_concern = models.ForeignKey(SkinConernModel, on_delete=models.CASCADE)
    react_to_new_products = models.ForeignKey(ReactToNewProductsModel, on_delete=models.CASCADE)
    sleep_cycle = models.ForeignKey(SleepCycleModel, on_delete=models.CASCADE, blank=True)
    skincare_texture = models.ForeignKey(SkinCareTextureModel, on_delete=models.CASCADE)
    essentials = models.TextField()
    image1 = models.ImageField(upload_to=facewash_image)
    image2 = models.ImageField(upload_to=facewash_image)
    description = models.TextField()

    def __str__(self):
        # return str([self.essentials, self.image1, self.image2, self.description])
        return self.skin_type.skin_type

    
    class Meta:
        ordering = ['id']
