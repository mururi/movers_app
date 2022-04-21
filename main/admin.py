from django.contrib import admin
from .models import Booking, Profile, Mover, User


# Register your models here.
admin.site.register(Profile)
admin.site.register(Mover)
admin.site.register(User)
admin.site.register(Booking)