from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password' , write_only=True)
    email = serializers.EmailField(source='user.email')
    # this for blank picture (till found another solution)
    picture = serializers.ImageField(allow_null=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username','password', 'email','birth_date','picture','country','address','slug')
        read_only_fields = ('slug',)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['user']['username'],
                                        email=validated_data['user']['email'],
                                        password=validated_data['user']['password'])

        user_model = UserModel.objects.create(user=user,
                                             birth_date=validated_data['birth_date'],
                                             picture=validated_data['picture'],
                                             country=validated_data['country'],
                                             address=validated_data['address'],
                                             )
        return user_model

    # def update(self, instance, validated_data):
    #     password = validated_data['user'].get('password', None)
    #     print(password)
    #     return
#
# class PasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ('password')
#         write