from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TempleViewSet,
    TempleGalleryImageViewSet,
    ArchitectureFeatureViewSet,
    ProductViewSet,
    ProductImageViewSet,
)

router = DefaultRouter()
router.register(r'temples', TempleViewSet)
router.register(r'temple-gallery-images', TempleGalleryImageViewSet)
router.register(r'architecture-features', ArchitectureFeatureViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
