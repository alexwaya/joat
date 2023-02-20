from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='pages-home'),
    path('members/', all_members, name='all_members'),
]