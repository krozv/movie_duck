from django.db import models
from django.conf import settings

# 영화 어떤 정보 받을 것인지 확인해야 함
class Movie(models.Model):
    title = models.CharField(max_length=200)  # 제목
    overview = models.TextField()   # 상세 설명
    movie_id = models.IntegerField()  # 영화 검색용 아이디
    adult = models.BooleanField() # 성인 영화 유무
    genre_id = models.JSONField()
    popularity = models.IntegerField()
    
    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['-created_at']  # 최신 글이 먼저 나오도록 정렬

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 일시
    updated_at = models.DateTimeField(auto_now=True)  # 최근 수정 일시
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)