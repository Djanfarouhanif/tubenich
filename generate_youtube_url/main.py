from googleapiclient.discovery import build
from video.models import Video_long_format, Video_petit_format, Video_list, Youtubeur
import time
import isodate


api_key = 'AIzaSyAYaYNBCibmanBU9NHpo2iFNkO7VJhXi58'

youtube = build('youtube', 'v3', developerKey=api_key)
#Fonction pour recuper toute les formations sur les video
def get_youtube_resutls(query, max_results):
   

    
    request = youtube.search().list(
        part = 'snippet',
        q = query,
        type = 'video',
        relevanceLanguage = 'fr',
        order = 'relevance',
        publishedAfter = '2017-01-01T00:00:00Z',
        maxResults = max_results,
        videoDuration = 'long'
    )
    response = request.execute()
    time.sleep(1)

    return response

#Fonction pour retourner les details sur la video
def video_response(data):
    video_id = [item['id']['videoId'] for item in data['items']]

    video_request = youtube.videos().list(
        part = 'contentDetails, snippet',
        id = ','.join(video_id)
    )
    video_response = video_request.execute()
    time.sleep(1)
    return video_response

#Fonction pour converture les duree iso 8601 en secondes
def fonction_pour_convertire_en_seconde(duration):
    
    parsed_duration = isodate.parse_duration(duration)

    return int(parsed_duration.total_seconds())
#Fonction pour retouner le nom de la chaine
def channelName(chaineId):
    request = youtube.channels().list(
        part = 'snippet',
        id = chaineId
    )
    response = request.execute()
    accountName = response['items'][0]['snippet']['title']

    return accountName
#Parcours les résultats et afficher les informations des videos d'au moin de une heure
def find_resutls(videos ,langagePrograming):
    video_response =videos

    for item in video_response['items']:

        id = item['id']
        channelId = item['snippet']['channelId']
        duration = item['contentDetails']['duration']
        duration_seconds = fonction_pour_convertire_en_seconde(duration)
        #Verifier si l'utilisateur exists ou non
        accountName = channelName(channelId)
        if Youtubeur.objects.filter(username=accountName).exists():
            currentaccount = Youtubeur.objects.get(username=accountName)
        else:
            newYoutubeur = Youtubeur.objects.create(username=accountName)
            newYoutubeur.save()

            currentaccount = Youtubeur.objects.get(username=accountName)
            
        if duration_seconds <= 3600 : #filtrer les videos d'au moins une heure
            print("==============================")
            accountUser = currentaccount
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnails = item['snippet']['thumbnails']
            default_thumbnail = thumbnails['default']['url']
            medium_thumbnail = thumbnails['medium']['url']
            high_thumbnail = thumbnails['high']['url']
            langage  = langagePrograming
            new_video_l = Video_petit_format.objects.create(accountUser=accountUser, title=title,thumbnails=thumbnails,programingLangage=langagePrograming, videoId=id, description=description)
            new_video_l.save()

        elif duration_seconds >= 3600:
            pri("***************")
            accountUser = currentaccount
            title = item['snippet']['title']
            description = item['snippet']['description']
            #recuper la minature
            thumbnails = item['snippet']['thumbnails']
            high_thumbnails = thumbnails['high']['url']
            
            new_video_p = Video_long_format.objects.create(accountUser=accountUser, title=title, videoId=id, thumbnails=thumbnails, description=description,programingLangage=langagePrograming)
            new_video_p.save()


