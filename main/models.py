from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField



# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    is_customer = models.BooleanField(default=False)
    is_mover = models.BooleanField(default=False)

    REQUIRED = []

    def __str__(self):
        return f'{self.username}User'

    def save_user(self):
        super().save()

    @classmethod
    def get_user(cls):
        user=User.objects.all()
        return user

    def delete_user(self):
        self.delete()

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    contact= models.IntegerField(null=True)
    profile_picture = CloudinaryField('profile_picture', default='default.png', null=True)


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


        
class Booking(models.Model):
    HOUSE_TYPES = [
        ('BS', 'Bedsitter'),
        ('OB', 'Onebedroom'),
        ('TB', 'Twobedroom'),
        ('SD', 'Studio'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    vacation_date = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)
    new_location = models.CharField(max_length=50)
    description = models.TextField()
    house = models.CharField(max_length=2, choices=HOUSE_TYPES)
    mover = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.user} {self.booking_date}'

class Mover(models.Model):
     
    id =  models.IntegerField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='selected_movers')
    price= models.IntegerField(blank=True)
    status=models.BooleanField()


    # @receiver(post_save, sender=User)
    # def create_user_move(sender, instance, created, **kwargs):
    #     if created:
    #         Mover.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_move(sender, instance, **kwargs):
    #     instance.move.save()  

   
    def save_user_move(sender, instance, **kwargs):
        instance.move.save()  