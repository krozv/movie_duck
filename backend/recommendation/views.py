from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from movie.serializers import MovieListSerializer, MovieSerializer
from movie.serializers import CommentSerializer, ReplySerializer
from movie.serializers import CommentReplySerializer
from movie.models import Movie, Comment, Reply
from django.shortcuts import get_object_or_404
from random import sample

@api_view(['GET', 'POST', 'PUT'])
def index(request):
  # 영화 추천 페이지: random 영화 목록 20개
  if request.method == 'GET':
    movies = Movie.objects.all()
    random_movies = sample(list(movies), 20)
    serializer = MovieListSerializer(random_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  # 요청 받은 영화 목록을 바탕으로 추천 영화 응답
  if request.method == 'POST':
    pass
  # 새로운 Random 영화 목록 20개 -> get이랑 비슷한데 굳이?
    