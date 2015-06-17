from django.contrib.auth.models import User
from rest_framework import serializers
from userapp.serializers import UserSerializer
from project.models import Project, Post, Contributor



class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ('id', 'name', 'project', 'is_pm', 'position')
        read_only_fields = ('project', 'name')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'project', 'text')
        read_only_fields = ('project')


class ProjectSerializer(serializers.ModelSerializer):
    PM = UserSerializer(read_only=True)
    modelslug = serializers.SlugField(read_only=True, source='slug')
    posts = PostSerializer(many=True, read_only=True)
    contributors = ContributorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'PM', 'title', 'description', 'plan', 'logo' , 'modelslug', 'posts', 'contributors')
        read_only_fields = ('PM', 'posts', 'contributors')