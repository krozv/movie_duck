from django.db import models
from django.conf import settings

# 영화 어떤 정보 받을 것인지 확인해야 함
class Genre(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=20)

class Actor(models.Model):
    actor_id = models.IntegerField()
    actor_name = models.CharField(max_length=100)
    actor_original_name = models.CharField(max_length=100)
    actor_popularity = models.IntegerField()
    profile_logo_path = models.TextField()

class Director(models.Model):
    director_id = models.IntegerField()
    director_name = models.CharField(max_length=100)
    director_original_name = models.CharField(max_length=100)
    director_popularity = models.IntegerField()

class Producer(models.Model):
    producer_id = models.IntegerField()
    producer_name = models.CharField(max_length=100)
    producer_original_name = models.CharField(max_length=100)
    producer_popularity = models.IntegerField()

class Provider(models.Model):
    provider_id = models.IntegerField()
    provider_name = models.CharField(max_length=50)
    provider_logo_path = models.TextField()

class Video(models.Model):
    video_id = models.CharField(max_length=100)
    video_key = models.CharField(max_length=100)
    video_name = models.TextField()
    video_site = models.CharField(max_length=50)
    official = models.BooleanField()
    video_type = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=200)  # 제목
    overview = models.TextField()   # 상세 설명
    movie_id = models.IntegerField()  # 영화 검색용 아이디
    adult = models.BooleanField() # 성인 영화 유무
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)
    producer = models.ManyToManyField(Producer)
    video = models.ManyToManyField(Video)
    Provider = models.ManyToManyField(Provider)
    popularity = models.IntegerField()
    poster_path = models.TextField()
    
    def __str__(self):
        return self.title

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