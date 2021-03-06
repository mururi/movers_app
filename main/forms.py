
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Mover, Profile, Booking



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'move')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'move')





class MoverForm(forms.ModelForm):
    class Meta:
        model = Mover
        exclude = ('user', 'move')

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user']
