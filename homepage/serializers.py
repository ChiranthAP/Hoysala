from rest_framework import serializers
from .models import Temple, TempleGalleryImage, ArchitectureFeature, Product, ProductImage

class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temple
        fields = '__all__'

class TempleGalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempleGalleryImage
        fields = '__all__'

class ArchitectureFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureFeature
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__' 