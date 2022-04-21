from django.urls import path, include
from . import views
from .views import RegisterView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('make-booking/', views.make_booking, name='make-booking'),
    path('register', RegisterView.as_view()),
    path('mover', views.mover, name='mover'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )