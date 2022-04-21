
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookingForm, UpdateProfileForm
from rest_framework.views import APIView
from main.serializers import UserSerializer
from rest_framework.response import Response

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

# Create a Registration view
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
