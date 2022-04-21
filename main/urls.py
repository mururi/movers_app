from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    
    path('', views.make_booking, name='make-booking'),
    path('register', 'RegisterView.as_view()'),
]