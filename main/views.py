
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.views import APICiew
# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
