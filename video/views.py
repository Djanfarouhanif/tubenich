from django.shortcuts import render
from .models import Video_long_format, Video_petit_format
from generate_youtube_url.main import get_youtube_resutls, video_response
# from generate_youtube_url.main import get_youtube_resutls ,fonction_pour_convertire_en_seconde, video_response  ,find_resutls
# # Create your views here.

# all_video_youtube = get_youtube_resutls("variable en python", 5)

# details_video = video_response(all_video_youtube)
data = get_youtube_resutls("python programming", 3)
print(video_response(data))

# resulta_final = find_resutls(details_video)
def index(request):
    return