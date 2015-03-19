from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers
from userapp.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    # date_joined = serializers.DateField(source='user.date_joined')
    picture = serializers.ImageField(required=False)
    birth_date = serializers.DateField()
    country = serializers.CharField()
    address = serializers.CharField()
    slug = serializers.SlugField(read_only=True)


    # picture = serializers.Field(source='picture')
    # birth_date = serializers.Field(source='birth_date')
    # country = serializers.Field(source='country')
    # address = serializers.Field(source='address')
    # slug = serializers.Field(source='slug')

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'picture', 'birth_date', 'country', 'address', 'slug', 'password')
        # write_only_fields = ('password',)
        # read_only_fields = ('slug',)
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True,
        #     },
        # }


    # def restore_object(self, attrs, instance=None):
    #     """
    #     Given a dictionary of deserialized field values, either update
    #     an existing model instance, or create a new model instance.
    #     """
    #     if instance is not None:
    #         instance.user.email = attrs.get('user.email', instance.user.email)
    #         instance.user.password = attrs.get('user.password', instance.user.password)
    #         instance.picture = attrs.get('picture', instance.picture)
    #         instance.birth_date = attrs.get('birth_date', instance.birth_date)
    #         instance.country = attrs.get('country', instance.country)
    #         instance.address = attrs.get('address', instance.address)
    #         return instance

    #     user = User.objects.create_user(username=attrs.get('user.username'), email= attrs.get('user.email'), password=attrs.get('user.password'))
    #     return UserModel(user=user)
