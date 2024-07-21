from googleapiclient.discovery import build
import time
import isodate


api_key = 'AIzaSyAYaYNBCibmanBU9NHpo2iFNkO7VJhXi58'

youtube = build('youtube', 'v3', developerKey=api_key)

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


def video_response(data):
    video_id = [item['id']['videoId'] for item in data['items']]

    video_request = youtube.videos().list(
        part = 'contentDetails, snippet',
        id = ','.join(video_id)
    )

    video_response = video_request.execute()

    return video_response
#Fonction pour converture les duree iso 8601 en secondes
def fonction_pour_convertire_en_seconde(duration):
    
    parsed_duration = isodate.parse_duration(duration)

    return int(parsed_duration.total_seconds())
#Parcours les résultats et afficher les informations des videos d'au moin de une heure
def find_resutls(videos):
    video_response =videos

    for item in video_response['items']:
        duration = item['contentDetails']['duration']
        duration_seconds = fonction_pour_convertire_en_seconde(duration)

        if duration_seconds >= 3600: #filtrer les videos d'au moins une heure
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnails = item['snippet']['thumbnails']
            default_thumbnail = thumbnails['default']['url']
            medium_thumbnail = thumbnails['medium']['url']
            hight_thumbnail = thumbnails['high']['url']

            print(f'Title: {title}')
            print(f'Description: {description}')
            print(f'Duration: {duration}')
            print(f'meduim thumbnail: {medium_thumbnail}')
            print(f'default thumbnais: {default_thumbnail}')
            print(f'high Thumbnails: {hight_thumbnail}')

