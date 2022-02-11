from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Reply, Survey, Question, Answer, FinalComment


class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = '__all__'

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    survey = SurveySerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):

    class Meta:

        model = Reply
        fields = '__all__'

class FinalCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalComment
        fields = '__all__'