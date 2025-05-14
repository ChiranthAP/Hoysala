from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'overview', 'highlights']
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at']

class TempleGalleryImageViewSet(viewsets.ModelViewSet):
    queryset = TempleGalleryImage.objects.all()
    serializer_class = TempleGalleryImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['temple']

class ArchitectureFeatureViewSet(viewsets.ModelViewSet):
    queryset = ArchitectureFeature.objects.all()
    serializer_class = ArchitectureFeatureSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'short_description', 'full_description']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['-created_at']

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product'] 