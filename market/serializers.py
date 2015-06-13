from django.contrib.auth.models import User
from rest_framework import serializers
from market.models import App, AppRating, AppComment, AppTransaction
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


class AppTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppTransaction
        fields = ('id', 'owner', 'app', 'unique_id', 'home_no', 'phone_no', 'delivery_address', 'delivery_time', 'purchase_time')
        read_only_fields = ('owner', 'app',)


class BuyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppTransaction
        fields = ('id', 'owner', 'app', 'unique_id', 'home_no', 'phone_no', 'delivery_address', 'delivery_time', 'purchase_time')
        read_only_fields = ('owner', 'app', 'unique_id')

class AppSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    comments = AppCommentSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)
    ratings = AppRatingSerializer(many=True, read_only=True)

    class Meta:
        model = App
        fields = ('id', 'owner', 'name', 'picture', 'description', 'price', 'ratings', 'comments', 'tags', 'avg_rating', 'transactions', 'url',)
        read_only_fields = ('owner', 'transactions', 'ratings')
