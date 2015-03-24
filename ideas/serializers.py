from django.contrib.auth.models import User
from rest_framework import serializers
from userapp.models import UserProfile
from ideas.models import Idea


class IdeaSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')

    class Meta:
        model = Idea
        fields = ('id', 'owner', 'title', 'description', 'rating', 'modelslug')
