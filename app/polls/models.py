from django.db import models
from app.core import settings


class Polls(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateTimeField(editable=False)
    end_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: ({self.start_date} - {self.end_date})'


class Questions(models.Model):
    TEXT = 1
    SINGLE = 2
    MULTIPLE = 3
    QUESTION_TYPES = (
        (TEXT, 'Text answer'),
        (SINGLE, 'Single choice'),
        (MULTIPLE, 'Multiple choices'),
    )

    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='questions')
    kind = models.IntegerField(choices=QUESTION_TYPES)
    text = models.TextField()


class Variants(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='variants')


class UserAnswers(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='user_answers')
    choice = models.ForeignKey(Variants, on_delete=models.CASCADE, related_name='user_answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=1000)
