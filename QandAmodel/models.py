from django.db import models
from django.contrib.auth import authenticate
from datetime import datetime
from django.conf import settings
from django.db.models import DateTimeField
from django.contrib.postgres.fields import ArrayField

User = settings.AUTH_USER_MODEL
# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default=list, null=True)
    tags = ArrayField(models.CharField(max_length=200, unique=False,
                      blank=True), unique=False, blank=True, default=list)
    body = models.TextField()
    slug = models.SlugField(
        max_length=250, unique_for_date='published', default="slug")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def __str__(self):
        return self.title


# Creating the answer model

class Answer(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    answer_text = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='answers_upvotes')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
