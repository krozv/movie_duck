from rest_framework import serializers
from .models import Movie, Comment, Reply, Boxoffice, Genre, Provider, Video
from accounts.models import User

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class RecommendListSerializer(serializers.ModelSerializer):
    recommend = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title', 'movie_id', 'poster_path', 'pk']
        fields.append('recommend')

    def get_recommend(self, obj):
        return self.context.get('recommend', 'default')

class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','user_profile']
        
class CommentSerializer(serializers.ModelSerializer):
    author = UserCommentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    author = UserCommentSerializer(read_only=True)
    class Meta:
        model = Reply
        fields = '__all__'

# movie 단일 serializer
class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    genres = MovieGenreSerializer(many=True, read_only=True)
    video = MovieVideoSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        # fields = ['title', 'overview', 'poster_path', 'comments']
        fields = '__all__'

# comment serializer

        
class CommentReplySerializer(serializers.ModelSerializer):
    
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class BoxOfficeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'overview', 'movie_id', 'poster_path', 'pk']

class BoxOfficeListSerializer(serializers.ModelSerializer):
    movie = BoxOfficeMovieSerializer(many=True, read_only=True)
    class Meta:
        model = Boxoffice
        fields = '__all__'