from community import serializers
from community.models import Review, Comment
from movies.models import Movie
from community.serializers import ReviewSerializer,  ReviewListSerializer, CommentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import get_user_model



class ReviewList(APIView):
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print('포스트 들어옴')
        serializer = ReviewSerializer(data=request.data)
        print(serializer)
        print('시리얼라이저 완료')
        if serializer.is_valid():
            serializer.save(user=request.user, movie=Movie.objects.get(pk=request.data['movie']['id']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


class ReviewClap(APIView):
    def post(request, pk):
        review = generics.get_object_or_404(Review, pk = pk)
        if review.claps.filter(pk=request.user.pk).exist():
            review.claps.remove(request.user)
        else:
            review.claps.add(request.user)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    


class Comment(APIView):
    def post(self, request, pk, format=None):
        serializer = CommentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(user=request.user, review = Review.objects.get(pk=pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

