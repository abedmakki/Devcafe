from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from userapp.models import UserModel
from userapp.serializers import UserSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class UserList(generics.ListCreateAPIView):
    """
    List all Users, or create a new User.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a User.
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
