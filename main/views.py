
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.views import APIView


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

# Create a Registeration view
class RegisterView(APIView):
    def post(self, request):
        pass
