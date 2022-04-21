
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import BookingForm

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

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