from django.db import models
from accounts.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 일시
    updated_at = models.DateTimeField(auto_now=True)  # 최근 수정 일시
    
    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ['-created_at']  # 최신 글이 먼저 나오도록 정렬

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 일시
    updated_at = models.DateTimeField(auto_now=True)  # 최근 수정 일시
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)