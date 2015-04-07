from django.contrib.auth.models import User
from ideas.serializers import IdeaSerializer, IdeaCommentSerializer
from ideas.models import Idea, IdeaComment
from rest_framework import generics
from rest_framework import permissions
from ideas.permissions import IsOwnerOrReadOnly


class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class IdeaCommentList(generics.ListCreateAPIView):
    queryset = IdeaComment.objects.all()
    serializer_class = IdeaCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IdeaCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IdeaComment.objects.all()
    serializer_class = IdeaCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

