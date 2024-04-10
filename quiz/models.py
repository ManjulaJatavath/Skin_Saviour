from django.db import models

# Create your models here.

class QuizModel(models.Model):
    treatment = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    skin_type = models.CharField(max_length=255)
    skin_concerns = models.CharField(max_length=255)
    react_to_new_products = models.CharField(max_length=255)
    sensitive = models.CharField(max_length=255)
    sleep_cycle = models.CharField(max_length=255)
    skincare_texture = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.treatment
    
    class Meta:
        ordering = ['id']
