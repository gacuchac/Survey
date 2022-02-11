
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['id']

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Survey(models.Model):
    class Meta:
        verbose_name = _("Survey")
        verbose_name_plural = _("Surveys")
        ordering = ['id']

    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Survey Title"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        return self.title

class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"),auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']

    SCALE = (
        (0, _("Fundamental")),
        (1, _("Begginer")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert"))
    )

    TYPE = (
        (0, _("Multiple Choice")),
    )

    survey = models.ForeignKey(Survey, related_name='question', on_delete=models.CASCADE)
    #technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
    #difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Level of Difficulty"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))
    always = models.BooleanField(default=False, verbose_name=("Always Ask"))

    def __str__(self):
        return self.title

class Answer(Updated):

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)
    #image = models.ImageField(upload_to='images/', default='images/default.png')
    image_url = models.CharField(max_length=255, verbose_name='image_url', default='https://drive.google.com/uc?export=view&id=14fX5yGbI0xrApvbx58fXkqequoyBSY9Z')
    #date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        return self.answer_text

class Reply(models.Model):
    class Meta:
        verbose_name = _("Reply")
        verbose_name_plural = _("Replies")
        ordering = ['id']
    
    answer = models.ForeignKey(Answer, related_name='reply', on_delete=models.DO_NOTHING)
    comment = models.CharField(max_length=255, verbose_name=_("Comment Text"), default="")
    knowledge_scale = models.IntegerField(default=0)
    reason = models.CharField(max_length=255, default="")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

class FinalComment(models.Model):
    class Meta:
        verbose_name = _("Final Comment")
        verbose_name_plural = _("Final Comments")
        ordering = ['id']
    
    final_comment = models.CharField(max_length=255, verbose_name=_("Final Comment Text"), default="")
    survey = models.ForeignKey(Survey, related_name='survey', on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))