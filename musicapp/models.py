from django.db import models

# Create your models here.
def audio_directory_path(instance, filename):
    # filename = TODO : logic to change your filename
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'audio/'+" secrets.token_urlsafe(11)"+'.mp3'
class MusicmindTrack(models.Model):
    track_file = models.FileField(upload_to=audio_directory_path)
    song_title = models.CharField(max_length=300)
    soundsource_id = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    composer = models.CharField(max_length=300)

    album = models.ForeignKey("musicmindalbum",related_name="mm_tracks", on_delete=models.SET_NULL, blank=True, null=True)
    artist = models.ForeignKey("musicmindartist", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.song_title

def album_cover_directory_path(instance, filename):
    # filename = TODO : logic to change your filename
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'album_covers/'+ "secrets.token_urlsafe(11)"+'.png'

class MusicmindAlbum(models.Model):
    album = models.CharField(max_length=300,null=True,blank=True)
    Photo = models.ImageField(upload_to=album_cover_directory_path, null=True, blank=True)
    artist = models.ForeignKey("musicmindartist",related_name="mm_albums", on_delete=models.CASCADE, null=True, blank=True)
    mbid = models.CharField(max_length=37,blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.album
    
    class Meta:
        ordering = ["album"]

class MusicmindArtist(models.Model):
    artist = models.CharField(max_length=300)
    objects = models.Manager()
    Photo = models.ImageField(upload_to='artist_covers', blank=True, null=True)

    def __str__(self):
        return self.artist


class MusicmindTrackDetails(models.Model):
    mmTrack = models.ForeignKey("musicmindtrack", on_delete=models.CASCADE, null=True, blank=True,unique=True)
    genre = models.CharField(max_length=300,blank=True, null=True)
 