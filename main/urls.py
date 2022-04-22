from atexit import register
from django.urls import path, include
from . import views
from .views import RegisterView, LoginView, UserView, LogoutView, VerifyEmailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('make-booking/', views.make_booking, name='make-booking'),
    path('reg', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='log'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('email_verify/', VerifyEmailView.as_view(), name='email_verify'),
    path('register/', views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )