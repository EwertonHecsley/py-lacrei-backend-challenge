from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from professionals.views import ProfessionalViewSet, ConsultationViewSet

router = routers.DefaultRouter()
router.register(r'professionals', ProfessionalViewSet)
router.register(r'consultations', ConsultationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
