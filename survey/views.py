from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Survey, Question
from .serializers import QuestionSerializer, SurveySerializer
from rest_framework.views import APIView

# Create your views here.

class Survey(generics.ListAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class SurveyQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(survey__title=kwargs['topic']).order_by('?')#[:1]
        serializer = QuestionSerializer(question, many=True)

        return Response(serializer.data)

