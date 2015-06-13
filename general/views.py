from general.serializers import TagSerializer
from general.models import Tag
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import permissions


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

class CreateTag(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def post(self, request):
        try:
            tag = Tag.objects.get(name=request.data['name'])
        except Exception, e:
            Tag.objects.create(name=request.data['name'])
            return Response(status=status.HTTP_201_CREATED)
            # raise e
        return Response(status=status.HTTP_200_OK)
