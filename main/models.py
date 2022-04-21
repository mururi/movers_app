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
        
class Booking(models.Model):
    class HouseTypes(models.TextChoices):
        BEDSITTER = 'BS', _('Bedsitter')
        ONEBEDROOM = 'OB', _('Onebedroom')
        TWOBEDROOM = 'TB', _('Twobedroom')
        STUDIO = 'SD', _('Studio')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacation_date = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)
    new_location = models.CharField(max_length=50)
    description = models.TextField()
    house = models.CharField(max_length=2, choices=HouseTypes.choices)
    mover = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.user} {self.booking_date}'
