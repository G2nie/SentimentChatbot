# chatbot/urls.py
from django.urls import include, path

urlpatterns = [
    path('', include('bot.urls')),
    path('', include('emotion.urls')), # emotion 앱 urls 추가
]
