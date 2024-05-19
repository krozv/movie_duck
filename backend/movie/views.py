from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import MovieListSerializer, MovieSerializer
from .serializers import CommentSerializer, ReplySerializer
from .serializers import CommentReplySerializer, BoxOfficeListSerializer
from .models import Movie, Comment, Reply, Actor, Producer, Director, Genre, Provider, Video, Boxoffice
from django.shortcuts import get_object_or_404
from pprint import pprint
from crawling import crawling, kobis_crawling, model_save
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def movie_main(request):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  # 데이터 추출 및 저장용으로 사용할 예정
  if request.method == 'POST':

    return Response({'message':'기능없음'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

@api_view(['GET'])
def box_office(request):
  if request.method == 'GET':
    movies = Boxoffice.objects.all()
    serializer = BoxOfficeListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)