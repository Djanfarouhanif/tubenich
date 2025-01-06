from rest_framework import serializers
from .models import Video, VideoProgress
from useraccount.serializer import UserSerializer

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

class VideoProgressSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    video = VideoSerializer()

    class Meta:
        model = VideoProgress
        fields = '__all__'