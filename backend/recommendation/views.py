from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from movie.serializers import MovieListSerializer, RecommendListSerializer
from movie.models import Movie, Genre, Actor, Director
from random import sample
from django.db.models import Count, F
from collections import defaultdict
from pprint import pprint

@api_view(['GET'])
def index(request):
  # 영화 추천 페이지: random 영화 목록 20개
  if request.method == 'GET':
    movies = Movie.objects.all()
    random_movies = sample(list(movies), 20)
    serializer = MovieListSerializer(random_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
# 요청 받은 영화 목록을 바탕으로 추천 영화 응답
@api_view(['POST'])
def genre(request):
  if request.method == 'POST':
    # user가 선택한 영화 목록 받음 -> 추후 저장할 것
    like_movies = request.data.get('userLikeMovies')
    
    # 영화 추천 알고리즘 짜기
    # 사용자가 선호하는 장르 2가지 
    genres = Movie.objects.filter(movie_id__in=like_movies).values('genres').annotate(total=Count('id')).order_by('-total')[:2]

    if len(genres) < 2:
      return Response({"error": "Not enough data to make recommendations"}, status=status.HTTP_400_BAD_REQUEST)
    
    recommendations = {}
    for genre in genres:
        genre_pk = genre.get('genres')
        genre = Genre.objects.get(pk=genre_pk)
        genre_movies = Movie.objects.filter(genres=genre).order_by('-popularity')[:5]
        genre_serializer = RecommendListSerializer(genre_movies, many=True, context={'recommend': genre.genre_name})
        recommendations[genre.genre_name] = genre_serializer.data
    return Response(recommendations, status=status.HTTP_200_OK)

@api_view(['POST'])
def actor(request):
  if request.method == 'POST':
    # user가 선택한 영화 목록 받음 -> 추후 저장할 것
    like_movies = request.data.get('userLikeMovies')
    
    # 영화 추천 알고리즘 짜기
    # 사용자가 선호하는 배우 2명 선정
    actors_query = Actor.objects.filter(movie__movie_id__in=like_movies).distinct().annotate(total=Count('id')).order_by('-total', '-actor_popularity')[:2]
    
    if len(actors_query) < 2:
        return Response({"error": "Not enough data to make recommendations"}, status=status.HTTP_400_BAD_REQUEST)

    recommendations = {}

    for actor in actors_query:
        print(actor.actor_name)
        print(actor.pk)
        print(actor.actor_id)
        print(actor)
        print(Movie.objects.filter(actors=actor))
        print(actor.pk)
        for movie in Movie.objects.filter(actors=actor):
           print(movie)

        # actor_movies = Movie.objects.filter(actors=actor).order_by('-popularity')[:5]
        # actor_serializer = RecommendListSerializer(actor_movies, many=True, context={'recommend': actor.actor_name})
        # print(actor_serializer)
        # recommendations[actor.actor_name] = actor_serializer.data
    pprint(recommendations)
    # Flatten the dictionary to a list
    # total_actor_data = [movie for movies in recommendations.values() for movie in movies]
    # pprint(total_actor_data)
    return Response(recommendations, status=status.HTTP_200_OK)
  
@api_view(['POST'])
def director(request):
  # user가 선택한 영화 목록 받음 -> 추후 저장할 것
  like_movies = request.data.get('userLikeMovies')
  
  # 영화 추천 알고리즘 짜기
  # 사용자가 선호하는 배우 2명 선정
  directors_query = Director.objects.filter(movie__movie_id__in=like_movies).distinct().annotate(total=Count('id')).order_by('-total', '-actor_popularity')
  
  first_director = directors_query[0]
  second_director = directors_query[1]