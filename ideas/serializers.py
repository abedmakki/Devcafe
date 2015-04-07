from django.contrib.auth.models import User
from rest_framework import serializers
from ideas.models import Idea


class IdeaSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')

    class Meta:
        model = Idea
        fields = ('id', 'owner', 'title', 'description', 'rating', 'modelslug')
        read_only_fields = ('owner',)
