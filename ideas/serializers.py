from django.contrib.auth.models import User
from rest_framework import serializers
from ideas.models import Idea, IdeaComment, IdeaRating , IdeaLike
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
    owner = UserSerializer(read_only=True)

    class Meta:
        model = IdeaComment
        fields = ('id', 'text', 'timestamp', 'owner')
        read_only_fields = ('timestamp', 'owner')


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
    is_liked = serializers.SerializerMethodField('get_pm_status')
    # rating = serializers.StringRelatedField(many=True)
    # ratings = IdeaRatingSerializer(many=True, read_only=True)
    def get_pm_status(self, obj):
        user = self.context['request'].user
        try:
            idealiked = IdeaLike.objects.get(owner=user, idea=obj)
            if idealiked:
                return True
        except IdeaLike.DoesNotExist:
            return False
    class Meta:
        model = Idea
        fields = ('id', 'owner', 'title', 'description', 'timestamp', 'likes', 'modelslug', 'comments', 'tags', 'avg_rating','is_liked')
        read_only_fields = ('owner','is_liked',)

