# Generated by Django 4.0 on 2022-01-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_alter_reply_answer_finalcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalcomment',
            name='knowledge_scale',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='finalcomment',
            name='reason',
            field=models.CharField(default='', max_length=255),
        ),
    ]
