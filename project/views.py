from project.serializers import ProjectSerializer, PostSerializer, \
    TaskSerializer, PostJobSerializer, \
    PostTaskSerializer, RequestSerializer
from project.models import Project, Post, Contributor, Task, Job, Request
from rest_framework import generics
from rest_framework.views import APIView
from project.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(PM=self.request.user)

    def post(self, request):
        project = Project(title=request.data['title'],
                          description=request.data['description'],
                          plan=request.data.get('plan', ''), PM=request.user)
        project.save()
        serializer = ProjectSerializer(project)
        Contributor.objects.create(
            user=self.request.user,
            project=project,
            is_pm=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CreateJob(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        if request.user == project.PM:
            job = PostJobSerializer(data=request.data)
            if job.is_valid():
                job.save(project=project)
                return Response(job.data, status=status.HTTP_201_CREATED)
            return Response(job.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AssignTask(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        #project = Project.objects.get(id=pk)
        contributor = Contributor.objects.get(id=pk)
        #if contributor.project == project:
        if request.user == contributor.project.PM:
            task = PostTaskSerializer(data=request.data)
            if task.is_valid():
                task.save(project=contributor.project, issued_to=contributor)
                return Response(task.data, status=status.HTTP_201_CREATED)
            return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
        #return Response(status=status.HTTP_404_NOT_FOUND)


class ApplyForJob(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        try:
            job = Job.objects.get(id=pk)
            job_request = Request.objects.filter(owner=request.user, job=job)
            if job_request.exists():
                if job.is_taken:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_200_OK)
            new_req = Request(owner=request.user, job=job)
            new_req.save()
            serializer = RequestSerializer(new_req)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


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


class ResolveRequests(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk, ans):
        try:
            req = Request.objects.get(pk=pk)
            if ans == '1':
                job = req.job
                if not job.is_taken:
                    job.is_taken = True
                    job.issued_to = req.owner
                    job.save()
                    contr = Contributor(job=job, user=req.owner, project=job.project, is_pm=False)
                    # Contributor.objects.create(job=job, user=req.owner, project=job.project, is_pm=False)
                    contr.save()
                    serializer = ContributorSerializer(contr)
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    # job is already taken
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif ans == '0':
                req.delete()
                return Response(status=status.HTTP_200_OK)

        except Exception, e:
            # return Response(status=status.HTTP_404_NOT_FOUND)
            raise e


class ViewMyTasks(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            contributor = Contributor.objects.get(user=request.user,
                                                  project=project)
            task = Task.objects.filter(project=project, issued_to=contributor)
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        except Contributor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
