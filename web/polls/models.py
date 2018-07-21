from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    text = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    slug= models.SlugField()

    def user_can_vote(self,user):
        user_vote = user.vote_set.all()
        qs = user_vote.filter(Poll=self)
        if qs.exists():
            return False
        else:
            return True




    def __str__(self):
        return self.text



class Choice(models.Model):
    poll= models.ForeignKey(Poll,on_delete=models.CASCADE)
    answer = models.TextField(max_length=200)

    def __str__(self):
        return self.answer

class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)