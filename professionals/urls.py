from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProfessionalViewSet

router = DefaultRouter()
router.register(r'professionals', ProfessionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
