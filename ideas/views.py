from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ideas.serializers import IdeaSerializer
from ideas.models import Idea
from rest_framework import generics


class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def perform_create(self, serializer):
        serializer.save(slug=slugify(serializer.data.get('title')))


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
