from googleapiclient.discovery import build
from video.models import Video_long_format, Video_petit_format, Video_list, Youtubeur
import time
import isodate


api_key = 'AIzaSyAYaYNBCibmanBU9NHpo2iFNkO7VJhXi58'

youtube = build('youtube', 'v3', developerKey=api_key)
#Fonction pour recuper toute les formations sur les video
def get_youtube_resutls(query, total_results):
    max_results_per_request = 50
    all_videos = []
    responses = []
    next_page_token = None
    while len(all_videos) < total_results:

        try:
            request = youtube.search().list(
                part = 'snippet',
                q = query,
                type = 'video',
                relevanceLanguage = 'fr',
                order = 'relevance',
                publishedAfter = '2017-01-01T00:00:00Z',
                maxResults = max_results_per_request,
                videoDuration = 'long',
                pageToken =next_page_token
            )
            response = request.execute()
            all_videos.extend(response['items'])
            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break
            time.sleep(1)
        
            responses.append(response)
        except Exception as e: 
            break
    return responses

#Fonction pour retourner les details sur la video
def video_response(datas):
    all_video_response = []
    if datas:
        for data in datas:
            if data:
                video_id = [item['id']['videoId'] for item in data['items']]

                video_request = youtube.videos().list(
                    part = 'contentDetails, snippet',
                    id = ','.join(video_id)
                )
                video_response = video_request.execute()
                time.sleep(1)
                all_video_response.append(video_response)

        return all_video_response
    else:
        return None

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
    try:
        for video in videos:
            video_response =video
            
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
                    if Video_petit_format.objects.filter(videoId=id).exists():
                        
                        pass
                    else:
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
                    if Video_long_format.objects.filter(videoId=id).exists():
                        
                        pass
                    else:
                        accountUser = currentaccount
                        title = item['snippet']['title']
                        description = item['snippet']['description']
                        
                        #recuper la minature
                        thumbnails = item['snippet']['thumbnails']
                        high_thumbnails = thumbnails['high']['url']
                        
                        new_video_p = Video_long_format.objects.create(accountUser=accountUser, title=title, videoId=id, thumbnails=thumbnails, description=description,programingLangage=langagePrograming)
                        new_video_p.save()
                    
    except:     
        return None



