from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

# 사용자가 입력한 메시지를 받아온 후,
# 메시지를 분석하여 가장 유사한 대답을 찾아서 리턴

def sentiment_chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        # 모델과 데이터 로드
        model = SentenceTransformer('jhgan/ko-sroberta-multitask')
        df = pd.read_csv('D:\python\Sentimentchatbot\wellness_dataset.csv')
        df['embedding'] = df['embedding'].apply(json.loads)

        # sentenceTranformer 모델을 이용하여 사용자가 입력한 문장의 임베딩 계산
        # 임베딩 = 텍스트 데이터를 벡터 형태로 변환
        embedding = model.encode(user_input)

        # cosine similarity
        # 유사도 계산 후 가장 유사한 문장 선택
        df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
        answer = df.loc[df['distance'].idxmax()]

        # 선택된 문장을 반환
        return JsonResponse({'result': answer['챗봇']},
                            json_dumps_params={'ensure_ascii': False})

    return render(request, 'emotion.html')