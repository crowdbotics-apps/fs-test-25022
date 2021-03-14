from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ItemVariantViewSet,
    CountryViewSet,
    ItemViewSet,
    CategoryViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register("item", ItemViewSet)
router.register("country", CountryViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("category", CategoryViewSet)
router.register("review", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
