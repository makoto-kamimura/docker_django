from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # view_main
    path('', views.main, name='main'),
]