from django.contrib import admin
from .models import Profile, Score, Question, Image, Answer

# Register your models here.
admin.site.register(Profile)
admin.site.register(Score)
admin.site.register(Question)
admin.site.register(Image)
admin.site.register(Answer)
