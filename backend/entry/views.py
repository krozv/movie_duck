from rest_framework.response import Response
from rest_framework import status
from .serializers import EntryListSerializer, EntrySerializer
from rest_framework.decorators import api_view
from .models import Entry, Comment, Reply
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def entry_main(request):
    # 전체 게시글 read
    if request.method == 'GET':
        articles = Entry.objects.all()
        serializer = EntryListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시글 create
    if request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def entry_detail(request, entry_pk):
    # 단일 게시글 read
    if request.method == 'GET':
        try:
            entry = get_object_or_404(Entry, pk=entry_pk)
            serializer = EntrySerializer(entry)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 읽으려는 게시글이 없을 때 Error 처리
        except:
            return Response({'error': '존재하지 않는 게시글'}, status=status.HTTP_404_NOT_FOUND)
    
    # 단일 게시글 update
    if request.method == 'PUT':
        pass