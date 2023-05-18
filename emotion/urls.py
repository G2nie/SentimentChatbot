from django.urls import path
from . import views

urlpatterns = [
    path('emotion/', views.sentiment_chatbot, name='sentiment_chatbot'),
]
