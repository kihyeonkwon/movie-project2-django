from rest_framework import serializers
from django.contrib.auth.models import User

from movies.models import Movie, Genre




class MovieListSerializer(serializers.ModelSerializer):
   
  genre_ids = serializers.StringRelatedField(many=True)   

  # class ReviewSerializer()
  class Meta:
    model = Movie
    fields =('id', 'title', 'genre_ids', 'poster_path')


class MovieSerializer(serializers.ModelSerializer):
      
  genre_ids = serializers.StringRelatedField(many=True)    

  # class ReviewSerializer()
  class Meta:
    model = Movie
    fields ='__all__'