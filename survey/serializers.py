from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Reply, Survey, Question, Answer, FinalComment


class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = [ 'id', 'title',]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id','image','image_url','answer_text','is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    survey = SurveySerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = ['id','survey','title','answer', ]

class ReplySerializer(serializers.ModelSerializer):

    class Meta:

        model = Reply
        fields = '__all__'

class FinalCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalComment
        fields = '__all__'