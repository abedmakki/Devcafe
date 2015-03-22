from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics , status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from userapp.models import UserModel
from userapp.serializers import UserSerializer

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

    def destroy(self, request, *args, **kwargs):
        try:
            usermodel = UserModel.objects.get(id=kwargs['pk'])
            user = usermodel.user
            usermodel.delete()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:return Response(status=status.HTTP_404_NOT_FOUND)

    ##need more work
    def update(self, request, *args, **kwargs):
        data=request.data
        try:
            snippet = UserModel.objects.get(pk=kwargs['pk'])
            nativep = snippet.user.password
        except UserModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        password = data.get('password',None)
        serializer = UserSerializer(snippet,data,partial=True)
        if serializer.is_valid():
            if password:
                serializer.save()
                return Response(serializer.data)
            else:
                print('none password')

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
