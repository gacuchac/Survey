from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display =['name',]


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields =['answer_text','is_right','image_url']
    extra = 0

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'survey','is_active','always']
    list_display =['id','title','survey','date_created','is_active','always']
    inlines = [AnswerInlineModel,]
    
@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display =['id','question','answer_text','is_right','image_url']

@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id','answer_id','answer','comment','knowledge_scale','reason','date_created']

    def answer_id(self, obj):
       return obj.answer_id
    answer_id.short_description = 'Answer ID'

class QuestionInlineModel(admin.TabularInline):
    model = models.Question
    fields = ['title', 'survey','is_active']
    inlines = [AnswerInlineModel,]
    extra = 0

@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display =['id','title','category','date_created']
    inlines = [QuestionInlineModel,]

@admin.register(models.FinalComment)
class FinalCommentAdmin(admin.ModelAdmin):
    list_display = ['id','survey','final_comment','date_created']