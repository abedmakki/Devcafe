from django.contrib.auth.models import User
# from django.forms import widgets
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'picture', 'birth_date', 'date_joined', 'country', 'address')
