from django.contrib.auth.models import User
from rest_framework import serializers
from ideas.models import Idea, IdeaComment
from userapp.serializers import UserSerializer


class IdeaCommentSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = IdeaComment
        fields = ('id', 'owner', 'timestamp', 'text')
        read_only_fields = ('owner',)


class IdeaSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')
    comments = IdeaCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Idea
        fields = ('id', 'owner', 'title', 'description', 'rating', 'modelslug', 'comments')
        read_only_fields = ('owner',)

