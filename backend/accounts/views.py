from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@authentication_classes([])
@permission_classes([])
@api_view(['POST'])
def user_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginAPIView(APIView):
    def post(self, request):
        # 사용자가 제공한 username과 password 가져오기
        username = request.data.get('username')
        password = request.data.get('password')

        # 사용자 인증
        user = authenticate(username=username, password=password)

        # 인증이 성공하면 토큰 생성
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            # 인증 실패시 에러 메시지 반환
            return Response({'error': '인증 실패'}, status=status.HTTP_401_UNAUTHORIZED)
