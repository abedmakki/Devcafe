from django.contrib.auth.models import User
from rest_framework import serializers
from ideas.models import Idea, IdeaComment, IdeaRating
from userapp.models import UserProfile
from userapp.serializers import UserSerializer
from general.serializers import TagSerializer


class IdeaCommentSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = IdeaComment
        fields = ('id', 'owner', 'timestamp', 'text', 'idea')
        read_only_fields = ('owner',)


class PostIdeaCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaComment
        fields = ('id', 'text')


class IdeaRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaRating
        fields = ('value',)


class RateIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaRating
        fields = ('id', 'value')


class IdeaSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')
    comments = IdeaCommentSerializer(many=True, read_only=True)
    # tags = TagSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()
    # rating = serializers.StringRelatedField(many=True)
    # ratings = IdeaRatingSerializer(many=True, read_only=True)

    class Meta:
        model = Idea
        fields = ('id', 'owner', 'title', 'description', 'timestamp', 'likes', 'modelslug', 'comments', 'tags', 'avg_rating')
        read_only_fields = ('owner',)

