from rest_framework import serializers
from .models import User
from movie.serializers import BoxOfficeMovieSerializer

class UserSerializer(serializers.ModelSerializer):
    user_liked_movie = BoxOfficeMovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'user_liked_movie', 'user_profile')  # Serializer에 포함할 필드 지정

