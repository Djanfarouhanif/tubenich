from django.shortcuts import render, redirect
from .models import Video_long_format, Video_petit_format
from django.http import HttpResponse
from useraccount.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from generate_youtube_url.main import get_youtube_resutls ,fonction_pour_convertire_en_seconde, video_response  ,find_resutls
# # Create your views here.

@login_required(redirect_field_name= 'login')
def loader(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        langage = request.POST.get('langage')
        number = request.POST.get('number')
        number_int = int(number)
        all_video_youtube = get_youtube_resutls(search, number_int)

        details_video = video_response(all_video_youtube)

        resulta_final = find_resutls(details_video, langage)
        redirect('loader')
    else:
        messages.info(request, 'Errore in your request')
        return redirect('loader')

    return None
#loader()
@login_required(redirect_field_name='login')
def index(request):
    return HttpResponse("<h1>salut</h1>")


# def findRsulte(request, user):
#     currentUser = request.user
    