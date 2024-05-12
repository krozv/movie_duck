from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
@permission_classes([])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': '회원가입 성공'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = get_user_model().objects.get(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'login 성공'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': '로그인 불가'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def user_logout(request):
    key = request.data['token']
    token, created = Token.objects.get_or_create(key=key)
    if token:
        token.delete()
        return Response({'message':'logout 성공'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': '토큰 없음'}, status=status.HTTP_204_NO_CONTENT)
    
def user_signout(request):
    pass