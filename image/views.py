from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ImageSerializer
from .models import ImageModel
# Create your views here.
class ImageView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer