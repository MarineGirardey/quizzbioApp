# Generated by Django 3.2.5 on 2021-11-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzbioApp', '0007_auto_20211111_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user_id',
        ),
        migrations.AddField(
            model_name='score',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
