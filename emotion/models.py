from django.db import models

# 모델 정의
class Sentiment(models.Model):
    user_input = models.TextField() # 사용자의 입력 저장
    bot_response = models.TextField() # 챗봇의 응답 저장
    date_created = models.DateTimeField(auto_now_add=True) # 대화 날짜 저장

    # 문자열 반환
    def __str__(self):
        return f"User Input: {self.user_input}, Bot Response: {self.bot_response}, Date: {self.date_created}"
