from django.contrib.auth.models import User
from market.serializers import AppSerializer, RateAppSerializer, PostAppCommentSerializer, AppCommentSerializer
from market.models import App, AppRating, AppComment
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from ideas.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg


class AppList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class Rate(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        app = App.objects.get(id=pk)
        rating = RateAppSerializer(data=request.data)
        if rating.is_valid():
            rating.save(app=app, owner=request.user)
            total_rating = app.ratings.all().aggregate(Avg('value'))
            app.avg_rating = total_rating['value__avg']
            app.save()
            return Response(rating.data, status=status.HTTP_201_CREATED)
        return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)


class AppCommentList(generics.ListAPIView):
    queryset = AppComment.objects.all()
    serializer_class = AppCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AppCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppComment.objects.all()
    serializer_class = AppCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class AddComment(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        app = App.objects.get(id=pk)
        comment = PostAppCommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save(app=app, owner=request.user)
            return Response(comment.data, status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)
