from rest_framework import serializers
from .models import Addition

class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = '__all__'
