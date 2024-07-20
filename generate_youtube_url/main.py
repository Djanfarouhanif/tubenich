from googleapiclient.discovery import build
import time

api_key = 'AIzaSyAYaYNBCibmanBU9NHpo2iFNkO7VJhXi58'

youtube = build('youtube', 'v3', developerKey=api_key)

def get_youtube_resutls(query, max_results):
    results = []

    next_page_token = None
    while len(results) < max_results:
        try:
            request = youtube.search().list(
                part = 'snippet',
                q = query,
                type = 'video',
                maxResutls = min(max_results - len(results), 50),
                pageToken = next_page_token
            )
            response = request.execute()
            results.exend(response['items'])
            if not next_page_token:
                break

        except Exception as e:
            print(f"An error occured: {e}")
            break

    return results