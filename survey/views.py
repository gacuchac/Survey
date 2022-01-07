from django.db import models
from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from .models import Reply, Survey, Question
from .serializers import QuestionSerializer, ReplySerializer, SurveySerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets

# Create your views here.

class Survey(generics.ListAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class SurveyQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(survey__title=kwargs['topic']).order_by('?')#[:1]
        serializer = QuestionSerializer(question, many=True)

        return Response(serializer.data)

    """ def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 """
class ReplyViewset(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer = ReplySerializer

@api_view(['POST'])
def replyCreate(request):
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


