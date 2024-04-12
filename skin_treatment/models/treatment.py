from django.db import models

class TreatmentModel(models.Model):
    treatment = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.treatment

class SkinTypeModel(models.Model):
    skin_type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.skin_type
    
class AgeModel(models.Model):
    age = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.age

class SkinConernModel(models.Model):
    skin_concern = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.skin_concern
    
class ReactToNewProductsModel(models.Model):
    react_to_new_products = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.react_to_new_products
    
class SensitiveModel(models.Model):
    senstive = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.senstive}'

class SleepCycleModel(models.Model):
    sleep_cycle = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.sleep_cycle
    
class SkinCareTextureModel(models.Model):
    skin_texture = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.skin_texture