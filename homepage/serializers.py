from rest_framework import serializers
from .models import Temple, TempleGalleryImage, ArchitectureFeature, Product, ProductImage

class TempleGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempleGalleryImage
        fields = ['id', 'image_url', 'created_at']

class TempleSerializer(serializers.ModelSerializer):
    gallery_images = TempleGalleryImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Temple
        fields = [
            'id', 'name', 'overview', 'highlights', 
            'location_info', 'main_image_url', 
            'gallery_images', 'created_at', 'updated_at'
        ]

class ArchitectureFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureFeature
        fields = [
            'id', 'title', 'short_description', 
            'full_description', 'created_at'
        ]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'description', 
            'image_url', 'images', 'created_at', 
            'updated_at'
        ] 