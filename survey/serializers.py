from rest_framework import serializers
from survey.models import Survey

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('name',)