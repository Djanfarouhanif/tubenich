from django.shortcuts import render
from .models import Video_long_format, Video_petit_format
from django.http import HttpResponse

from generate_youtube_url.main import get_youtube_resutls ,fonction_pour_convertire_en_seconde, video_response  ,find_resutls
# # Create your views here.

all_video_youtube = get_youtube_resutls("variable en python", 5)

details_video = video_response(all_video_youtube)

resulta_final = find_resutls(details_video, 'Python')

def index(request):
    return HttpResponse("<h1>salut</h1>")