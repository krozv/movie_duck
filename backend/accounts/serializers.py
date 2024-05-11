from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 비밀번호 필드를 입력만 가능하도록 설정

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)  # Serializer에 포함할 필드 지정

    # def create(self, validated_data):
    #     # 비밀번호를 해싱하여 저장
    #     password = validated_data.pop('password')
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user
