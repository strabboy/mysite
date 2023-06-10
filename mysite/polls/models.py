from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=256)
    pub_dt = models.DateTimeField("Date of publication")


class Choice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
