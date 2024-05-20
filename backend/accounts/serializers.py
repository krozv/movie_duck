from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 비밀번호 필드를 입력만 가능하도록 설정

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)  # Serializer에 포함할 필드 지정

