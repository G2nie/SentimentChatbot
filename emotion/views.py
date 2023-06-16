from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

def sentiment_chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        model = SentenceTransformer('jhgan/ko-sroberta-multitask')
        df = pd.read_csv('D:\python\SentimentChatbot\wellness_dataset.csv')
        df['embedding'] = df['embedding'].apply(json.loads)

        # 사용자 입력 임베딩
        embedding = model.encode(user_input)

        df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
        answer = df.loc[df['distance'].idxmax()]

        # 구분 컬럼이 존재하는지 확인 후 반환
        sentiment = answer.get('구분', 'Unknown')

        result = answer['챗봇'] if '챗봇' in answer else 'Unknown'

        return JsonResponse({'result': result, 'sentiment': sentiment},
                            json_dumps_params={'ensure_ascii': False})

    return render(request, 'emotion.html')