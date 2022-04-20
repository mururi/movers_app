
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.



class Profile(models.Model):
    id =  models.IntegerField(primary_key=True)
    user_id= models.ForeignKey()(max_length=80, blank=True)
    contact= models.IntegerField()(max_length=254, blank=True)
    profile_picture = CloudinaryField('profile_picture', default='default.png')


    def __str__(self):
        return f'{self.user.id} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()  
   
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()  

class Mover(models.Model):
     
    id =  models.IntegerField(primary_key=True)
    booking_id= models.ForeignKey()(max_length=80, blank=True)
    price= models.IntegerField()(max_length=254, blank=True)
    status=models.BooleanField()


    @receiver(post_save, sender=User)
    def create_user_move(sender, instance, created, **kwargs):
        if created:
            Mover.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_move(sender, instance, **kwargs):
        instance.move.save()  

   
    def save_user_move(sender, instance, **kwargs):
        instance.move.save()  
