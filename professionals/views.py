from django.shortcuts import render

from rest_framework import viewsets
from .models import Professional,Consultation
from .serializers import ProfessionalSerializer, ConsultationSerializer

class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer