from django.urls import path
from django.urls.conf import include
from .views import Survey, SurveyQuestion, replyCreate
from .router import router

app_name='survey'

urlpatterns = [
    path('', Survey.as_view(), name='survey'),
    path('<str:topic>/', SurveyQuestion.as_view(), name='questions' ),
    path('reply/create/', replyCreate, name='create'),
]