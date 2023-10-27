from django.contrib import admin
from .models import MusicmindTrack,MusicmindAlbum,MusicmindArtist,MusicmindTrackDetails

# Register your models here.

admin.site.register(MusicmindTrack)
admin.site.register(MusicmindAlbum)
admin.site.register(MusicmindArtist)
admin.site.register(MusicmindTrackDetails)
