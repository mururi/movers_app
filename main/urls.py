from django.urls import path, include
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.index, name='index'),
    path('make-booking/', views.make_booking, name='make-booking'),
    path('register', 'RegisterView.as_view()'),
]
