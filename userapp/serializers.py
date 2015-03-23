from django.contrib.auth.models import User
from rest_framework import serializers
from userapp.models import UserProfile
from django.template.defaultfilters import slugify
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(UserDetailsSerializer):

    picture = serializers.ImageField(source="userprofile.picture", allow_null=True)
    birth_date = serializers.DateField(source="userprofile.birth_date")
    country = serializers.CharField(source="userprofile.country")
    address = serializers.CharField(source="userprofile.address")
    slug = serializers.CharField(source="userprofile.slug", allow_blank=True, read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('id', 'username', 'password', 'picture', 'birth_date', 'country', 'address', 'slug',)
        read_only_fields = ('slug',)
        write_only_fields = ('password',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        picture = profile_data.get('picture')
        birth_date = profile_data.get('birth_date')
        country = profile_data.get('country')
        address = profile_data.get('address')
        slug = profile_data.get('slug', None)

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data:
            if picture:
                profile.picture = picture
            if birth_date:
                profile.birth_date = birth_date
            if country:
                profile.country = country
            if address:
                profile.address = address
            # if slug:
            #     profile.slug = slug
            # else:
            #     profile.slug = slugify(username)
            profile.save()

        # userinstance = UserProfile(**profile)
        return instance


    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        picture = profile_data.get('picture')
        birth_date = profile_data.get('birth_date')
        country = profile_data.get('country')
        address = profile_data.get('address')
        slug = profile_data.get('slug', None)

        # print profile_data

        instance = super(UserSerializer, self).create(validated_data)
        # print instance

        useracc = UserProfile(picture=picture, birth_date=birth_date, country=country, address=address, user=User.objects.get(pk=instance.id))
        useracc.save()

        return instance
