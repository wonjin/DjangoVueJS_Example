from django.shortcuts import render
from rest_framework import viewsets
from survey.models import Survey
from survey.serializers import SurveySerializer
# Create your views here.

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

