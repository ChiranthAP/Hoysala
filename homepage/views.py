from django.shortcuts import render
from rest_framework import viewsets
from .models import Temple, TempleGalleryImage, ArchitectureFeature, Product, ProductImage
from .serializers import (
    TempleSerializer,
    TempleGalleryImageSerializer,
    ArchitectureFeatureSerializer,
    ProductSerializer,
    ProductImageSerializer,
)

# Create your views here.

def index(request): 
    return render(request, 'homepage/index.html', {}) 

class TempleViewSet(viewsets.ModelViewSet):
    queryset = Temple.objects.all()
    serializer_class = TempleSerializer

class TempleGalleryImageViewSet(viewsets.ModelViewSet):
    queryset = TempleGalleryImage.objects.all()
    serializer_class = TempleGalleryImageSerializer

class ArchitectureFeatureViewSet(viewsets.ModelViewSet):
    queryset = ArchitectureFeature.objects.all()
    serializer_class = ArchitectureFeatureSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer 