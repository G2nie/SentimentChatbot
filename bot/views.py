# bot/views.py
from django.shortcuts import render
from django.http import JsonResponse

def chatbot(request):
    # 챗봇 동작 로직 구현
    # ...
    response_data = {
        'result': '챗봇 응답, 아신기해'
    }
    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})

