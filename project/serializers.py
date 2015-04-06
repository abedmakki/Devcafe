from django.contrib.auth.models import User
from rest_framework import serializers
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')

    class Meta:
        model = Project
        fields = ('id', 'PM', 'title', 'description', 'plan', 'logo' , 'modelslug')
        read_only_fields = ('PM',)

