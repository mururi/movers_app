
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.views import APIView

from main.serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

# Create a Registration view
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

