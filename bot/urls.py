# bot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('bot/', views.chatbot, name='chatbot'),
]
