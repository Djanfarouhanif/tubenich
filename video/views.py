from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from .serializer import VideoSerializer, VideoProgressSerializer
from .models import Video, VideoProgress


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @action(detail=True, methods=['get'])
    def get_video(self, request, pk=None):
        try: 
            video = self.get_object()
            serilaier = self.get_serializer(video)
            return Response(serializer.data)

        except Video.DoesNotExist:
            raise NotFound("Vidoe introuvable")



class VideoProgressViewSet(viewsets.ModelViewSet):
    queryset = VideoProgress.objects.all()
    serializer_class = VideoProgressSerializer
