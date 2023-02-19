from django.urls import path
from .views import RegisterView 

from .views import profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
]