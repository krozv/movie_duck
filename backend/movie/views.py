from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer
from .serializers import CommentSerializer, ReplySerializer
from .serializers import CommentReplySerializer
from .models import Movie, Comment, Reply, Actor, Producer, Director
from django.shortcuts import get_object_or_404
from pprint import pprint
from crawling import crawling

@api_view(['GET', 'POST'])
def movie_main(request):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  # 데이터 추출 및 저장용으로 사용할 예정
  if request.method == 'POST':
    
    movies = Movie.objects.all()
    # 각 영화마다 영화 id 추출 range(1517, 2025)
    for movie_pk in range(1525, 1536):
      movie = Movie.objects.get(pk=movie_pk)
      credits = crawling.credits(movie.movie_id)
      if credits:
        casts = credits.get('cast')
        crews = credits.get('crew')
    # @ pprint(crews)
        for crew in crews:
          if crew.get('job') == 'Producer':
                pprint(crew.get('name'))
                producer_id = crew.get('id')
                query = f"SELECT * FROM movie_producer WHERE producer_id = {producer_id}"
                producers = Producer.objects.raw(query)

                if not producers:
                  print('없음')
                  producer = Producer.objects.create(
                    producer_id = producer_id,
                    producer_name = crew.get('name'),
                    producer_original_name = crew.get('original_name'),
                    producer_popularity = crew.get('popularity'),
                    )
                  movie.producer.add(producer)
                # actors가 있다면
                for producer in producers:
                  print(producer.id, producer.producer_id, producer.producer_name)  # 예시로 출력하는 필드들입니다.
                  movie.producer.add(producer)
          if crew.get('job') == 'Director':
              pprint(crew.get('name'))
              director_id = crew.get('id')
              query = f"SELECT * FROM movie_director WHERE director_id = {director_id}"
              directors = Director.objects.raw(query)

              if not directors:
                print('없음')
                director = Director.objects.create(
                  director_id = director_id,
                  director_name = crew.get('name'),
                  director_original_name = crew.get('original_name'),
                  director_popularity = crew.get('popularity'),
                  )
                movie.director.add(director)

              for director in directors:
                print(director.id, director.director_id, director.director_name)  # 예시로 출력하는 필드들입니다.
                movie.director.add(director)
        
        print('-------------------------')

    serializer = MovieListSerializer(movies, many=True)
    return Response(crews, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_pk):
  # 단일 게시글 (댓글 포함) 조회
  if request.method == 'GET':
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
@api_view(['POST'])
def create_comment(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  content = request.data.get('content')
  comment = Comment.objects.create(
    movie=movie,
    author=request.user,
    content=content
  )
  serializer = CommentSerializer(comment)
  return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def comment(request, movie_pk, comment_pk):
  # 댓글 조회(대댓글 포함)
  if request.method == 'GET':
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentReplySerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  # 댓글 수정
  if request.method == 'PUT':
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
  
  # 댓글 삭제
  if request.method == 'DELETE':
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  # 대댓글 생성
  if request.method == 'POST':
    comment = get_object_or_404(Comment, pk=comment_pk)
    content = request.data.get('content')
    reply = Reply.objects.create(
      comment=comment,
      author=request.user,
      content=content
    )
    serializer = ReplySerializer(reply)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def reply(request, movie_pk, comment_pk, reply_pk):
  # 대댓글 수정
  if request.method == 'PUT':
    reply = get_object_or_404(Reply, pk=reply_pk)
    serializer = ReplySerializer(reply, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
  
  # 대댓글 삭제
  if request.method == 'DELETE':
    reply = get_object_or_404(Reply, pk=reply_pk)
    reply.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
