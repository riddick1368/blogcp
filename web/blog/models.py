from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100,unique=True)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    slug = models.SlugField()
    active = models.BooleanField(default=True)



    def __str__(self):
        return self.title



class Postimage(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    image = models.ImageField()




