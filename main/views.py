import email
from lib2to3.pgen2 import token
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth import login, authenticate

from main import serializers
from .forms import BookingForm, UpdateProfileForm
from rest_framework.views import APIView
from main.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
import jwt, datetime
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.renderers import TemplateHTMLRenderer


def index(request):
    return render(request, 'index.html')

def profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    params = {
        'user_prof': user_prof,
    }
    return render(request, 'profile.html', params)

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {'form': form})



def make_booking(request):
    current_user = request.user
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit = False)
            booking.user = current_user
            booking.save()
        return redirect('/')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {"form": form})

    # The Registration of a user
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# Create a Registration view
class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email_verify')


        absurl = 'http://'+current_site+relativeLink+'?token='+ str(token)
        email_body = 'Hi '+user.username+'\n Kindly use the Link below to verify your Movers App. Account \n' + absurl
        data={'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}
        Util.send_email(data)

        return Response({'signup':user_data})

# Creating Email verification class
class VerifyEmailView(APIView):
    def get(self):
        pass

# Creating the Login View
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('The user was not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('The password provided is incorrect')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token
        }
        return response

# Creating the USer view
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!!')

        user = User.objects.filter(id=payload['id']). first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Logout View
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Success'
        }
        return response