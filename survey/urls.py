from django.urls import path
from .views import Survey, SurveyQuestion

app_name='survey'

urlpatterns = [
    path('', Survey.as_view(), name='survey'),
    path('<str:topic>/', SurveyQuestion.as_view(), name='questions' ),
]