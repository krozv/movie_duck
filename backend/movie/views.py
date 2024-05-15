from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer
from .models import Movie, Comment
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def movie_main(request):
  movies = Movie.objects.all()
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_pk):
  # 단일 게시글 (댓글 포함) 조회
  if request.method == 'GET':
    try: 
      movie = get_object_or_404(Movie, pk=movie_pk)
      serializer = MovieSerializer(movie)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except:
       return Response({'error':'존재하지 않는 영화'}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['PUT', 'DELETE', 'POST'])
def comment(request, movie_pk, comment_pk):
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