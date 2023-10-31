from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import MusicmindTrack,MusicmindArtist,MusicmindTrackDetails,MusicmindAlbum
from django.conf import settings
import psycopg2
import json
from .serializer import MusicmindTrackSerializer, MusicmindTrackDetailsSerializer
from django.core.serializers import serialize
import random


@csrf_exempt
def recommendation_new_user(request, *args, **kwargs):
    if request.method == 'GET':

        # same_artist = get_same_artist_songs_list(artist_id)
        # same_album = get_same_album_songs_list(album_id)
        new_list = get_newly_added_songs_list()

        data_response = get_datils_of_songs(new_list)
        return JsonResponse(data=data_response, safe=False)
    else:
        data_response = {"msg": "In Valid request type.", "error": True,}
        return JsonResponse(data=data_response, safe=False)
        
@csrf_exempt
def recommendation_ai(request, *args, **kwargs):
    if request.method == 'POST':

        # same_artist = get_same_artist_songs_list(artist_id)
        # same_album = get_same_album_songs_list(album_id)
        new_list = get_newly_added_songs_list()

        data_response = get_datils_of_songs(new_list)
        return JsonResponse(data=data_response, safe=False)
    else:
        data_response = {"msg": "In Valid request type.", "error": True,}
        return JsonResponse(data=data_response, safe=False)
    
def get_datils_of_songs(id_list):
    tracks = MusicmindTrackDetails.objects.filter(id__in=id_list) #[:200]
    serializer = MusicmindTrackDetailsSerializer(tracks, many=True)
    serialized_data = serializer.data
    count = len(serialized_data)
    if count < 10 or count < len(id_list)/2:
        tracks = MusicmindTrack.objects.filter(id__in=id_list) #[:200]
        serializer = MusicmindTrackSerializer(tracks, many=True)
        serialized_data = serializer.data
    count = len(serialized_data)
    data_response = {"msg": "Valid request type.", "error": False, 'Count': count, 'data': serialized_data}
    return data_response

def get_recent_listend_songs_list(user_id):
    recents_songs = []
    return recents_songs

def get_newly_added_songs_list():
    track_ids = MusicmindTrack.objects.all().order_by('-id').values_list('id', flat=True)[0:1000]
    shuffled_indices = random.sample(range(len(track_ids)), len(track_ids))
    shuffled_list = [track_ids[i] for i in shuffled_indices]
    return shuffled_list[:10]
    
    
def get_predicted_songs_list():
    predicted_songs = []
    return predicted_songs

def get_same_artist_songs_list(artist_id, album_id ):
    track_ids = MusicmindTrack.objects.filter(artist__id=artist_id).values_list('id', flat=True)[0:10]
    return track_ids

def get_same_album_songs_list(artist_id, album_id ):
    track_ids = MusicmindTrack.objects.filter(album__id=album_id).values_list('id', flat=True)[0:10]
    return track_ids