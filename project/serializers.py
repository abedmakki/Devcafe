from django.contrib.auth.models import User
from rest_framework import serializers
from userapp.serializers import UserSerializer
from project.models import Project, Post, Contributor, Task, Job



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'project', 'text')
        read_only_fields = ('project')


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'issued_to', 'project', 'is_done')
        read_only_fields = ('project', 'issued_to')


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'name', 'description', 'issued_to', 'project', 'is_taken')


class ContributorSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Contributor
        fields = ('id', 'name', 'project', 'is_pm', 'position', 'tasks')
        read_only_fields = ('project', 'name')


class ProjectSerializer(serializers.ModelSerializer):
    PM = UserSerializer(read_only=True)
    modelslug = serializers.SlugField(read_only=True, source='slug')
    posts = PostSerializer(many=True, read_only=True)
    contributors = ContributorSerializer(many=True, read_only=True)
    project_tasks = TaskSerializer(many=True, read_only=True)
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'PM', 'title', 'description', 'plan', 'logo' , 'modelslug', 'posts', 'contributors', 'project_tasks', 'jobs')
        read_only_fields = ('PM', 'posts', 'contributors', 'jobs')