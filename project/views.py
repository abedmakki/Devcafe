from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from project.serializers import ProjectSerializer, PostSerializer, ContributorSerializer, TaskSerializer, JobSerializer, PostJobSerializer
from project.models import Project, Post, Contributor, Task, Job
from project.models import Project
from rest_framework import generics
from rest_framework.views import APIView
from project.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(PM=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #def perform_create(self, serializer):
        #serializer.save(project=self.request.project)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RequestForJob(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def post(self, request, pk):
        project = Project.objects.get(id=pk)
        if request.user == project.PM:
            job = PostJobSerializer(data=request.data)
            if job.is_valid():
                job.save(project=project)
                return Response(job.data, status=status.HTTP_201_CREATED)
            return Response(job.error, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)