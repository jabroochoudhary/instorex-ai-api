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


@method_decorator(csrf_exempt, name='dispatch')
class RecommendationAI(View):
   def get(self, request, *args, **kwargs):
            # obj = MusicmindTrack.objects.all()[:10]
            # tracks = MusicmindTrack.objects.select_related('album', 'artist').all()[:200]
            tracks = MusicmindTrackDetails.objects.all()[:200]
            
            # json_data = serialize('json', tracks)
            serializer = MusicmindTrackDetailsSerializer(tracks, many=True)
            serialized_data = serializer.data
            # data = json.loads(json_data)
            data_response = {"msg":  "Valid request type." , "error":False, 'data':serialized_data}
            return JsonResponse(data=data_response)
    
   

    # def get_recent_song_list(user_id):
    #     recents_songs = []
    #     return recents_songs

    # def get_newly_added_songs_list():
    #     new_songs = []
    #     return new_songs
    
    # def getTables():
        
    #     return table_names
    
def get_predicted_songs_list():
    predicted_songs = []
    return predicted_songs