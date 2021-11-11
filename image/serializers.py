from .models import ImageModel
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.FileField(use_url=True)
    class Meta:
        model = ImageModel
        fields = ['image',]