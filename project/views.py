from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from project.serializers import ProjectSerializer, PostSerializer, ContributorSerializer, TaskSerializer, JobSerializer, PostJobSerializer, PostTaskSerializer, RequestSerializer
from project.models import Project, Post, Contributor, Task, Job, Request
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

    def post(self, request):
        project = Project(title=request.data['title'], description=request.data['description'], plan=request.data.get('plan', ''), PM=request.user)
        project.save()
        Contributor.objects.create(user=self.request.user, project=project, is_pm=True, position="Project Manager")
        return Response(status=status.HTTP_201_CREATED)


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


class AssignTask(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def post(self, request, pk, cont):
        project = Project.objects.get(id=pk)
        contributor = Contributor.objects.get(id=cont)
        if contributor.project == project:
            if request.user == project.PM:
                task = PostTaskSerializer(data=request.data)
                if task.is_valid():
                    task.save(project=project, issued_to=contributor)
                    return Response(task.data, status=status.HTTP_201_CREATED)
                return Response(task.error, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=statgus.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)

        # if request.user == project.PM:
        #     task = PostTaskSerializer(data=request.data)
        #     if task.is_valid():
        #         print task
        #         #task = PostTaskSerializer(data=request.data)
        #         if task.issued_to.project == pk:
        #             task.save(project=project)
        #             return Response(task.data, status=status.HTTP_201_CREATED)
        #         return Response(task.error, status=status.HTTP_400_BAD_REQUEST)
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # return Response(status=status.HTTP_404_NOT_FOUND)


class ApplyForJob(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def post(self, request, pk, jobID):
        try:
            job = Job.objects.get(id=jobID)
            job_request = Request.objects.filter(owner=request.user, job=job)
            if job_request.exists():
                return Response(status=status.HTTP_200_OK)
            Request.objects.create(owner=request.user, job=job)
            return Response(status=status.HTTP_201_CREATED)
        except Exception, e:
            raise e


class ViewRequests(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            if project.PM == request.user:
                req = Request.objects.filter(job__project=project)
                serializer = RequestSerializer(req, many=True)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception, e:
            raise e