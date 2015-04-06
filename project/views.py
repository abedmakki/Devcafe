from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from project.serializers import ProjectSerializer
from project.models import Project
from rest_framework import generics
from project.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


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
