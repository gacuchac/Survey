from rest_framework import serializers
from .models import Survey, Question, Answer


class SurveySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Survey
        fields = [
            'title',
        ]

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
        fields = [
            'survey','title','answer',
        ]