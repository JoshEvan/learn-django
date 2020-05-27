from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    # has column created_by as FK refrencing user_id on User table
    pub_date = models.DateTimeField(auto_now=True)
    # auto_now set field every time object saved, get updted too when Model.save()

    def __str__(self):
        # override tostring of model
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices',on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # UNIQUE statement at CREATE TABLE statement
        unique_together = ('poll','voted_by')
