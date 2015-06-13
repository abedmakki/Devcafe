from django.contrib.auth.models import User
from ideas.serializers import IdeaSerializer, IdeaCommentSerializer, PostIdeaCommentSerializer, RateIdeaSerializer
from ideas.models import Idea, IdeaComment, IdeaRating, IdeaLike
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from ideas.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg


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


class IdeaCommentList(generics.ListAPIView):
    queryset = IdeaComment.objects.all()
    serializer_class = IdeaCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IdeaCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IdeaComment.objects.all()
    serializer_class = IdeaCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class AddComment(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        idea = Idea.objects.get(id=pk)
        comment = PostIdeaCommentSerializer(data=request.data)
        if comment.is_valid():
            # comment.object.idea = idea
            # comment.object.owner = request.user
            comment.save(idea=idea, owner=request.user)
            return Response(comment.data, status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)
        # comment = IdeaComment.objects.create(text=request.data, owner=request.user, idea=idea)
        # comment.save()

        # return Response(IdeaCommentSerializer(comment), status=status.HTTP_201_CREATED)

class Rate(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        idea = Idea.objects.get(id=pk)
        # rating = RateIdeaSerializer(data=request.data)
        # if rating.is_valid():
        #     rating.save(idea=idea, owner=request.user)
        #     total_rating = idea.ratings.all().aggregate(Avg('value'))
        #     idea.avg_rating = total_rating['value__avg']
        #     idea.save()
        #     return Response(rating.data, status=status.HTTP_201_CREATED)
        # return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            own_rating = IdeaRating.objects.filter(owner=request.user, idea=idea)
            for rate in own_rating:
                rate.delete()
                rating = RateIdeaSerializer(data=request.data)
                if rating.is_valid():
                    rating.save(idea=idea, owner=request.user)
                    total_rating = idea.ratings.all().aggregate(Avg('value'))
                    idea.avg_rating = total_rating['value__avg']
                    idea.save()
                    return Response(rating.data, status=status.HTTP_201_CREATED)
                return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)
            rating = RateIdeaSerializer(data=request.data)
            if rating.is_valid():
                rating.save(idea=idea, owner=request.user)
                total_rating = idea.ratings.all().aggregate(Avg('value'))
                idea.avg_rating = total_rating['value__avg']
                idea.save()
                return Response(rating.data, status=status.HTTP_201_CREATED)
            return Response(rating.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception, e:
            raise e



class Like(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        idea = Idea.objects.get(id=pk)
        # if (own_like = IdeaLike.objects.get(owner=request.user, idea=idea).exists()):
        #     own_like.delete()
        #     return Response(status=status.HTTP_200_SUCCESS)
        # else:
        #     IdeaLike.objects.create(owner=request.user, idea=idea)
        #     return Response(status=status.HTTP_200_SUCCESS)
        try:
            own_like = IdeaLike.objects.filter(owner=request.user, idea=idea)
            for like in own_like:
                like.delete()
                return Response(status=status.HTTP_200_OK)
            IdeaLike.objects.create(owner=request.user, idea=idea)
            return Response(status=status.HTTP_200_OK)
            # else:
        except Exception, e:
            raise e
            # IdeaLike.objects.create(owner=request.user, idea=idea)
            # return Response(status=status.HTTP_200_OK)