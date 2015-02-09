from django.contrib import admin
from musicool.models import Album, Track, Playlist
# Register your models here.
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Playlist)