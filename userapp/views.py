from django.shortcuts import render
from django.contrib.auth.models import User ,AnonymousUser
from rest_framework import generics , status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from userapp.models import UserProfile
from userapp.serializers import UserSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin
from userapp.permissions import IsOwnerOrReadOnly


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
    permission_classes = (IsOwnerOrReadOnly,)


class GetUserProfile(generics.RetrieveAPIView):
    """
    Retrieve only the User who request
    """
    def retrieve(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)


class UpdateProfilePicture(generics.CreateAPIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        photo = request.FILES['file']
        if photo:
            try:
                profile = UserProfile.objects.get(user=user)
                profile.picture = photo
                profile.save()
                serializer = UserSerializer(profile.user)
            except UserProfile.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.data , status=status.HTTP_200_OK)



    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         usermodel = UserProfile.objects.get(id=kwargs['pk'])
    #         user = usermodel.user
    #         usermodel.delete()
    #         user.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except:return Response(status=status.HTTP_404_NOT_FOUND)

    ##need more work
    # def update(self, request, *args, **kwargs):
    #     data=request.data
    #     try:
    #         snippet = User.objects.get(pk=kwargs['pk'])
    #         nativep = snippet.user.password
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     password = data.get('password',None)
    #     serializer = UserSerializer(snippet,data,partial=True)
    #     if serializer.is_valid():
    #         if password:
    #             serializer.save()
    #             return Response(serializer.data)
    #         else:
    #             print('none password')

    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter
