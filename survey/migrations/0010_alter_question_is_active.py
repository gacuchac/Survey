# Generated by Django 4.0 on 2022-01-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_alter_answer_question_alter_question_survey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active Status'),
        ),
    ]
