import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MusicmindTrack,MusicmindArtist,MusicmindTrackDetails,MusicmindAlbum
import json
from .serializer import MusicmindTrackSerializer, MusicmindTrackDetailsSerializer
from django.core.serializers import serialize
import random

# these imports are used to get prediction from models
import re
from nltk.corpus import stopwords
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib



@csrf_exempt
def recommendation(request, *args, **kwargs):
    if request.method == 'GET':
        track_id = request.GET.get('track_id')
        if track_id is None:
            new_list = get_newly_added_songs_list(20)
            data_response = get_datils_of_songs(new_list)
        else:
            data = get_single_track_detail(track_id)
        # print(json.dumps(track_detail))
            album_id = data['album']['id']
            artist_id = data['artist']['id']
            genre = data['genre']
            album = data['album']['album']
            artist = data['artist']['artist']
        
            same_artist = get_same_artist_songs_list(artist_id)
            # print(len(same_artist))
            same_album = get_same_album_songs_list(album_id)
            # print(len(same_album))

            new_list = get_newly_added_songs_list(10)
            # print(len(new_list))

            model_list = get_model_prediction(artist, album, genre)


            combined_list = list(set(list(model_list) + list(new_list) + list(same_artist) + list(same_album)))
            result_list = list(combined_list)
            # print(len(result_list))
            data_response = get_datils_of_songs(result_list)

        return JsonResponse(data=data_response, safe=False)
    else:
        data_response = {"msg": "In Valid request type.", "error": True,}
        return JsonResponse(data=data_response, safe=False)
        
def get_single_track_detail(id):
    tracks = MusicmindTrack.objects.get(id=id) #[:200]
    serializer = MusicmindTrackSerializer(tracks)
    serialized_data = serializer.data
    return serialized_data

def get_datils_of_songs(id_list):
    tracks = MusicmindTrack.objects.filter(id__in=id_list) #[:200]
    serializer = MusicmindTrackSerializer(tracks, many=True)
    serialized_data = serializer.data
    count = len(serialized_data)
    data_response = {"msg": "Valid request type.", "error": False, 'Count': count, 'data': serialized_data}
    return data_response

def get_recent_listend_songs_list(user_id):
    recents_songs = []
    return recents_songs

def get_newly_added_songs_list(t):
    track_ids = MusicmindTrack.objects.all().order_by('-id').values_list('id', flat=True)[0:1000]
    shuffled_indices = random.sample(range(len(track_ids)), len(track_ids))
    shuffled_list = [track_ids[i] for i in shuffled_indices]
    return shuffled_list[:t]


def get_same_artist_songs_list(artist_id):
    track_ids = MusicmindTrack.objects.filter(artist__id=artist_id).values_list('id', flat=True)[0:10]
    return track_ids

def get_same_album_songs_list(album_id ):
    track_ids = MusicmindTrack.objects.filter(album__id=album_id).values_list('id', flat=True)[0:10]
    return track_ids

def preprocess_text(text):
    # nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def get_model_prediction(artist, album, genre):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model_files")
    print(path)
    artist = preprocess_text(artist)
    album = preprocess_text(album)
    genre = preprocess_text(genre)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_vectorizer = joblib.load(os.path.join(path,'tfidf_vectorizer.pkl'))
    input_vector = tfidf_vectorizer.transform([album + ' ' + artist + ' ' + genre])
    model_load = joblib.load(os.path.join(path,'kmeans_model_musicmind.pkl'))
    cluster = model_load.predict(input_vector)
    map_IDs =joblib.load(os.path.join(path,'map_prediction.pkl'))
    track_ids = [key for key, value in map_IDs.items() if value == cluster[0]]
    return track_ids[:30]