from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from . serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

User = get_user_model()


class SignOutView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        Token.objects.filter(user=user).delete()
        user.delete()
        request.session.flush()
        return JsonResponse({"message": "회원탈퇴 성공"})


class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserProfileview(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_pk, **kwargs):
        User = get_user_model()
        user = get_object_or_404(User, pk=user_pk)
        # 'profile' 필드를 직접 저장하는 경우, 이는 User 모델에 'profile' 필드가 있어야 합니다.
        # 또한, request.data.get('profile')가 올바른 형식이어야 합니다.
        if request.data.get('profile'):
            user.user_profile = request.data.get('profile')
            user.save()
            return Response({'message':'성공'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': '프로필 정보가 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)