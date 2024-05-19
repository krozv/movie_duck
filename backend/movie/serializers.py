from rest_framework import serializers
from .models import Movie, Comment, Reply, Boxoffice

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class RecommendListSerializer(serializers.ModelSerializer):
    recommend = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['title', 'movie_id', 'poster_path']
        fields.append('recommend')

    def get_recommend(self, obj):
        return self.context.get('recommend', 'default')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['title', 'overview', 'adult', 'comments']

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