from django.db import models

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