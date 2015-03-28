from django.contrib.auth.models import User
from rest_framework import serializers
from userapp.models import UserProfile
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')

    class Meta:
        model = Project
        fields = ('id', 'PM', 'title', 'description', 'plan', 'logo' , 'modelslug')