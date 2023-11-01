# from rest_framework import serializers
# from musicapp.models import MusicmindTrack, MusicmindAlbum, MusicmindArtist


# class musicmind_track_serializer(serializers.ModelSerializer):

    
#     #album = serializers.StringRelatedField(read_only=True)
#     album_name = serializers.ReadOnlyField(source="album.album")
#     album_photo = serializers.ImageField(source="album.Photo", read_only=True)
#     artist_name = serializers.ReadOnlyField(source="artist.artist")
#     #position = playlist_track_lookup()

#     class Meta:
#         model = MusicmindTrack
#         fields = ("id", "soundsource_id","track_file", "song_title", "album_photo", "album", "album_name", "artist", "artist_name")
#         read_only_fields = ['track_file',"song_title", "id"]
  

# class musicmind_track_serializer_export(serializers.ModelSerializer):

    
#     #album = serializers.StringRelatedField(read_only=True)
#     album_name = serializers.ReadOnlyField(source="album.album")
#     artist_name = serializers.ReadOnlyField(source="artist.artist")
#     #position = playlist_track_lookup()

#     class Meta:
#         model = MusicmindTrack
#         fields = ("id", "soundsource_id", "song_title", "album_name", "artist_name")
#         read_only_fields = ["song_title", "id"]
  
# class musicmind_album_serializer(serializers.ModelSerializer):
#     mm_tracks = musicmind_track_serializer(many=True, read_only=True)
#     class Meta:
#         model = MusicmindAlbum
#         fields = ("id","album", "artist","mm_tracks","Photo")

# class musicmind_artist_serializer(serializers.ModelSerializer):
#     mm_albums = musicmind_album_serializer(read_only=True, many=True)
#     class Meta:
#         model = MusicmindArtist
#         fields = ("id","artist","mm_albums","Photo")
        

# # class MusicmindTrackDetails(serializers.ModelSerializer):
# #     mmTrack = models.ForeignKey("MusicmindTrack", on_delete=models.CASCADE, null=True, blank=True,unique=True)
# #     genre = models.CharField(max_length=300,blank=True, null=True)
 



# //////////////////////////////////////////////////////////////

from rest_framework import serializers
from .models import MusicmindTrack
from .models import MusicmindTrack,MusicmindArtist,MusicmindTrackDetails,MusicmindAlbum


# Define serializers for related models
class MusicmindAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicmindAlbum
        fields = '__all__'

class MusicmindArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicmindArtist
        fields = '__all__'

class MusicmindTrackSerializer(serializers.ModelSerializer):
    album = MusicmindAlbumSerializer()  # Include the related album object
    artist = MusicmindArtistSerializer()  # Include the related artist object

    class Meta:
        model = MusicmindTrack
        fields = ("id", "soundsource_id", "track_file", "song_title", "album", "artist","genre","year","composer")
        read_only_fields = ["track_file", "song_title", "id"]
        
class MusicmindTrackDetailsSerializer(serializers.ModelSerializer):
    mmTrack = MusicmindTrackSerializer()
    class Meta:
        model = MusicmindTrackDetails
        fields = '__all__'
