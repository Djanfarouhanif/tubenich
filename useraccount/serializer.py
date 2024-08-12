from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'password']
        extra_kwargs = { 'password': {"write_only": True}}

    

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"],
            last_name = validated_data.get("last_name", '')
        )
        return user

class ProfileSerializers(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user', 'langage', 'profile_image']
        extra_kwargs = { "profile_image": {'required':False}}

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        
        profile = Profile.objects.create(user=user, **validated_data)

        return profile


