from rest_framework import serializers
from userapp.serializers import UserSerializer
from project.models import Project, Post, Contributor, Task, Job, Request


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
        read_only_fields = ('project', 'issued_to')


class ContributorSerializer(serializers.ModelSerializer):

    tasks = TaskSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Contributor
        fields = ('id', 'user', 'project', 'is_pm', 'tasks')
        read_only_fields = ('project', 'user')


class ProjectSerializer(serializers.ModelSerializer):
    PM = UserSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    # contributors = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=True)
    contributors = ContributorSerializer(many=True)
    project_tasks = TaskSerializer(many=True, read_only=True)
    jobs = JobSerializer(many=True, read_only=True)
    is_pm = serializers.SerializerMethodField('get_pm_status')
    is_contributor = serializers.SerializerMethodField('get_contributor_status')
    
    def get_pm_status(self, obj):
        user = self.context['request'].user
        if obj.PM == user:
            return True
        return False

    def get_contributor_status(self, obj):
        # return self.context['is_contributor']
        user = self.context['request'].user
        for contributor in obj.contributors.all():
            if contributor.user == user:
                return True
        return False

    class Meta:
        model = Project
        fields = ('id', 'PM', 'title', 'description', 'plan', 'logo',
                  'timestamp', 'posts', 'contributors', 'project_tasks',
                  'jobs', 'is_pm' ,'is_contributor')
        read_only_fields = ('PM', 'posts', 'contributors', 'jobs', 'is_pm', 'is_contributor')


class ProjectSerializerForNoncontibutor(serializers.ModelSerializer):
    PM = UserSerializer(read_only=True)
    jobs = JobSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'PM', 'title', 'description', 'logo', 'timestamp', 'jobs')
        read_only_fields = ('PM', 'jobs')


class PostJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'name', 'description')


class PostTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'title', 'description')


class RequestSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Request
        fields = ('id', 'owner', 'job')
        read_only_fields = ('owner', 'job')


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('logo','title')