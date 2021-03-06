# Generated by Django 4.0 on 2022-01-03 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_alter_answer_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='color',
            field=models.CharField(default='white', max_length=255),
        ),
        migrations.AlterField(
            model_name='answer',
            name='image_url',
            field=models.CharField(default='https://drive.google.com/uc?export=view&id=14fX5yGbI0xrApvbx58fXkqequoyBSY9Z', max_length=255, verbose_name='image_url'),
        ),
    ]
