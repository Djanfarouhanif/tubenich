from rest_framework import serializers
from .models import Video_long_format, Youtubeur

class YoutubeurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Youtubeur
        fields = ['url', 'username', 'follower']


class VideoLongFormatSerializer(serializers.HyperlinkedModelSerializer):
    accountUser  = serializers.PrimaryKeyRelatedField(queryset=Youtubeur.objects.all())
    class Meta:
        model = Video_long_format
        fields = ['accountUser', 'title', 'videoId', 'thumbnails', 'description', 'programingLangage']

class LoaderSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=255)
    langage = serializers.CharField(max_length=100)
    number = serializers.IntegerField()