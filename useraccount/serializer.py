from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username', 'email', 'last_name', 'password']
        extra_kwargs = { 'password': {"write_only": True}}

class ProfileSerializers(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['url','user', 'langage', 'profile_image']
        extra_kwargs = { "profile_image": {'required':False}}