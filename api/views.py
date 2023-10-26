from django.shortcuts import render
from django.http import JsonResponse


def recommendation_songs(req):
    if req.method == 'GET':
        print("Post Request")
        data_response = {"msg":  "Valid request type." , "error":False,}
        return JsonResponse(data=data_response)
    else:
        return JsonResponse(data= {"msg":  "Invalid request type." , "error":True,},)
    

def get_predicted_songs_list():
    predicted_songs = []
    return predicted_songs

def get_recent_song_list(user_id):
    recents_songs = []
    return recents_songs

def get_newly_added_songs_list():
    new_songs = []
    return new_songs

