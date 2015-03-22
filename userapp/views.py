from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics , status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from userapp.models import UserProfile
from userapp.serializers import UserSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin


class UserList(generics.ListCreateAPIView):
    """
    List all Users, or create a new User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a User.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            usermodel = UserProfile.objects.get(id=kwargs['pk'])
            user = usermodel.user
            usermodel.delete()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:return Response(status=status.HTTP_404_NOT_FOUND)

    ##need more work
    def update(self, request, *args, **kwargs):
        data=request.data
        try:
            snippet = UserProfile.objects.get(pk=kwargs['pk'])
            nativep = snippet.user.password
        except UserProfile.DoesNotExist:
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


# class FacebookLogin(SocialLogin):
#     adapter_class = FacebookOAuth2Adapter
