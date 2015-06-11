from django.contrib.auth.models import User
from rest_framework import serializers
from market.models import App, AppRating, AppComment
from userapp.models import UserProfile
from userapp.serializers import UserSerializer


class AppRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppRating
        fields = ('value',)


class RateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppRating
        fields = ('id', 'value')


class AppCommentSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = AppComment
        fields = ('id', 'owner', 'timestamp', 'text', 'app')
        read_only_fields = ('owner',)


class PostAppCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppComment
        fields = ('id', 'text')


class AppSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')
    owner = serializers.StringRelatedField()
    comments = AppCommentSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)
    ratings = AppRatingSerializer(many=True, read_only=True)

    class Meta:
        model = App
        fields = ('id', 'owner', 'name', 'picture', 'description', 'price', 'ratings', 'modelslug', 'comments', 'tags', 'avg_rating')
        read_only_fields = ('owner',)




