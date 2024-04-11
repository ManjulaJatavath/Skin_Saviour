from rest_framework import serializers

from quiz.models import QuizModel

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = [
            'id', 
            'preferred_skin_treatment', 
            'age', 
            'skin_type', 
            'skin_concerns', 
            'skin_react_to_new_products', 
            'sensitive',
            'sleep_cycle',
            'preferred_texture',
        ]