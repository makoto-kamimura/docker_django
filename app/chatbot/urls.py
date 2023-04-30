from django.urls import path
from . import views

urlpatterns = [
    path('', views.My_chat_botView.as_view(), name="my_chat_bot"),
]