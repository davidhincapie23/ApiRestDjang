from rest_framework import serializers
from .models import Balones

class Balonesserializers(serializers.ModelSerializer):
    class Meta:
        model = Balones
        fields = '__all__' 