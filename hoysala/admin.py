from django.contrib import admin
from homepage.models import Temple, TempleGalleryImage, ArchitectureFeature, Product, ProductImage

# The models are already registered in homepage/admin.py

@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'overview')
    list_filter = ('created_at', 'updated_at')

@admin.register(TempleGalleryImage)
class TempleGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('temple', 'created_at')
    list_filter = ('temple', 'created_at')
    search_fields = ('temple__name',)

@admin.register(ArchitectureFeature)
class ArchitectureFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'short_description')
    list_filter = ('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'price')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('product__name',) 