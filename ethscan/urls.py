from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('pie/', pie, name='pie'),
    path('line/', line, name='line'),
    
]
