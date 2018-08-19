from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class UserProfile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR  = 3
    Role_choice = (
        (STUDENT,'Student'),
        (TEACHER , 'Teacher'),
        (SUPERVISOR , "Supervisor"),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    name = models.CharField(max_length=120)
    family_name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    phone_number = models.IntegerField(default=0)
    description = models.TextField(max_length=500)
    role = models.PositiveSmallIntegerField(choices=Role_choice,blank=True,null=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username


    @receiver(post_save,sender=User)
    def CreateProfileUser(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)


