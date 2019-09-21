from rest_framework import serializers
from .models import abstractData

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = abstractData
        fields = '__all__'