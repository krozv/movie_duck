from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from movie.serializers import MovieListSerializer, MovieSerializer
from movie.serializers import CommentSerializer, ReplySerializer
from movie.serializers import CommentReplySerializer, RecommendListSerializer
from movie.models import Movie, Genre
from django.shortcuts import get_object_or_404
from random import sample
from django.db.models import Count, F

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
    # user가 선택한 영화 목록 받음 -> 추후 저장할 것
    like_movies = request.data.get('userLikeMovies')
    print(type(like_movies))
    
    # 영화 추천 알고리즘 짜기
    # 사용자가 선호하는 장르 2가지 
    movies = Movie.objects.filter(movie_id__in=like_movies)
    genre_result = movies.values('genres').annotate(total=Count('id')).order_by('-total')

    first_genre = Genre.objects.get(pk=genre_result[0]['genres'])
    second_genre = Genre.objects.get(pk=genre_result[1]['genres'])
    
    # 해당 장르의 영화 우선순위 기준으로 5개 추천
    first_genre_movies = Movie.objects.filter(genres=first_genre).order_by('-popularity')[:5]
    second_genre_movies = Movie.objects.filter(genres=second_genre).order_by('-popularity')[:5]
    
    first_genre_serializer = RecommendListSerializer(first_genre_movies, many=True, context={'recommend': first_genre.genre_name})
    first_genre_data = first_genre_serializer.data

    second_genre_serializer = RecommendListSerializer(second_genre_movies, many=True, context={'recommend': second_genre.genre_name})
    second_genre_data = second_genre_serializer.data

    total_genre_data = first_genre_data + second_genre_data
    return Response(total_genre_data, status=status.HTTP_200_OK)
  # 새로운 Random 영화 목록 20개 -> get이랑 비슷한데 굳이?
    