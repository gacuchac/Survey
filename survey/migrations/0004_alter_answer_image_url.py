# Generated by Django 4.0 on 2022-01-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_answer_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image_url',
            field=models.CharField(default='https://drive.google.com/file/d/14fX5yGbI0xrApvbx58fXkqequoyBSY9Z', max_length=255, verbose_name='image_url'),
        ),
    ]
