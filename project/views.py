from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from project.serializers import ProjectSerializer
from project.models import Project
from rest_framework import generics
from project.permissions import IsOwnerOrReadOnly


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsOwnerOrReadOnly,)
