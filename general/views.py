from general.serializers import TagSerializer
from general.models import Tag
from rest_framework import generics
# from rest_framework import permissions


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)