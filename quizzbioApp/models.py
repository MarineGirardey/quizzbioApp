from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Profile(models.Model):  # model - class    - table
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)  # field - instance - row
    imageField = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    points = models.IntegerField(null=True, blank=True)  # field - instance - row
    n_answer = models.IntegerField(null=True, blank=True)  # field - instance - row
    n_image = models.IntegerField(null=True, blank=True)  # field - instance - row


class Score(models.Model):  # model - class    - table
    score = models.IntegerField(null=True, blank=True)  # field - instance - row
    user_name = models.CharField(max_length=255, null=True, blank=True)


# Create your models here.
class Question(models.Model):                    # model - class    - table
    question = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    imageField = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    points = models.IntegerField(null=True, blank=True)  # field - instance - row
    nb_answer = models.IntegerField(null=True, blank=True)  # field - instance - row
    nb_image = models.IntegerField(null=True, blank=True)  # field - instance - row

    def __str__(self):
        return str(self.question)


class Answer(models.Model):  # model - class - table
    question_id = models.IntegerField(null=True, blank=True)  # field - instance - row
    answer = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    definition = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row

    def __str__(self):
        return str(self.answer)


class Image(models.Model):  # model - class    - table
    image_name = models.ImageField(upload_to="image/", max_length=255, null=True, blank=True)  # field - instance - row
    description = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    microscopy = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    cell_type = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    component = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    doi = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row
    organism = models.CharField(max_length=255, null=True, blank=True)  # field - instance - row

    resize_image = ImageSpecField(source='image_name',
                                  processors=[ResizeToFill(300, 300)],
                                  format='JPEG',
                                  options={'quality': 100})

    def __str__(self):
        return str(self.image_name)
