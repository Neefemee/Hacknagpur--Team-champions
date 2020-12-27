from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.utils.timezone import now

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default="")
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Answer(models.Model):
    text = models.TextField(default="")
    created_on = models.DateTimeField(default=now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
