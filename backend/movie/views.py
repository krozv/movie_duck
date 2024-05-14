from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Movie
from pprint import pprint
import json
# Create your views here.

def movie_main(request):
  # 현재 상영 중인 영화 데이터 -> 뷰에서 컴포넌트로 처리
  # 인기 영화 데이터 -> 뷰에서 컴포넌트로 처리
  pass

def movie_detail(request, movie_pk):
  
  pass


# dump data 만드는 기능
def request(request):
  return render(request, 'request.html')

def save(request):
  if request.method == 'POST':
    movies = json.loads(request.body)['movies']
    pprint(movies)
    for data in movies:
      movie = Movie(
        title = data['title'],
        overview = data['overview'],
        movie_id = data['id'],
        adult = data['adult'],
        genre_id = data['genre_ids'],
        popularity = data['popularity']
      )
      movie.save()
    return HttpResponse({'message': '성공'})
    # movies = json.loads(request.body)