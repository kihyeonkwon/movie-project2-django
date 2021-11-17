from rest_framework import serializers
from community.models import Review, Comment
from movies.models import Movie
from movies.serializers import MovieSerializer
from accounts.serializers import UserSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    claps_count = serializers.IntegerField(
        source='claps.count',
        read_only=True
    )
    class Meta:        
        model = Review
        fields = '__all__'
    


class ReviewSerializer(serializers.ModelSerializer):

    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')


    comments = CommentSerializer(many=True, read_only=True)
    movie = MovieSerializer(read_only=True)
    claps_count = serializers.IntegerField(
        source='claps.count',
        read_only=True
    )
    class Meta:
        model = Review
        read_only_fields = ('claps','user' )
        fields = ('movie', 'user', 'title', 'content', 'rank', 'claps', 'created_at', 'updated_at', 'comments', 'claps_count')


class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'content')
        read_only_fields = ('review','user')