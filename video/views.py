from django.shortcuts import render, redirect
from .models import Video_long_format, Video_petit_format
from django.http import HttpResponse
from useraccount.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from generate_youtube_url.main import get_youtube_resutls ,fonction_pour_convertire_en_seconde, video_response  ,find_resutls
#the imprt the rest_frameworks moduls
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializer import VideoLongFormatSerializer, LoaderSerializer,VideoSerializer

# i = Video_long_format.objects.all()
# for n in i:
#     print(n.videoId)

#Fonction pour telecharger les donnes youtube
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def loader(request):

    if request.method == 'POST':
        serializer  = LoaderSerializer(data=request.data)

        if serializer.is_valid():

            search = serializer.validated_data.get('search')
            langage = serializer.validated_data.get('langage')
            number = serializer.validated_data.get('number')
            
            all_video_youtube = get_youtube_resutls(search, number)

            details_video = video_response(all_video_youtube)

            resulta_final = find_resutls(details_video, langage)
            return Response(status=status.HTTP_200_OK)
        else:
        
            return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

#Fonction pour envoyer les informations stocker dans la base de donner 
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def index(request):
    video_long = Video_long_format.objects.all()
    serializer = VideoLongFormatSerializer(video_long, many=True, context={'request':request})

    return Response(serializer.data,status=status.HTTP_200_OK )


#Fonction pour recuper une vidoe
@api_view(['POST'])
def video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        video_info = Video_long_format.objects.get(videoId=serializer.validated_data.get('videoId'))
        print(video_info)
        
    return Response({'daa': "video_info"}, status=status.HTTP_200_OK)
    