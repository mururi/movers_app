from django.contrib import admin
from .models import Profile, Mover, User, Booking


# Register your models here.
admin.site.register(Profile)
admin.site.register(Mover)
admin.site.register(User)
admin.site.register(Booking)