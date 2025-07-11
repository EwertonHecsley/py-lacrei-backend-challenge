from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessionalViewSet, ConsultationViewSet

router = DefaultRouter()
router.register(r'professionals', ProfessionalViewSet)
router.register(r'consultations', ConsultationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
