from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from models import *
import spotipy
from spotify_util import *
from django.contrib.auth.decorators import login_required

def index(request):

    hot_albums = Album.objects.order_by('-likes')[:4]

    context_dict = {'hot_albums': hot_albums}
    return render(request, 'musicool/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'musicool/about.html', context_dict)



def album(request, album_id):
    pages = []
    album = get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album=album)

    context_dict = {'album': album, 'tracks': tracks}
    return render(request, 'musicool/album.html', context_dict)

@login_required
def spotify_ask_authorized(request):

    prompt_user_login(username=request.user.username)

    return redirect('/musicool/spotify_login/')

@login_required
def spotify_login(request):

    #  Get token
    if 'code' in request.GET:  # Retrieve token for the first time (No Cache)
        code = request.GET['code']
        token = exchange_token_with_code(code, username=request.user.username)
    else:  # Retrieve token from cache
        token = exchange_token_with_code(username=request.user.username)

    if token: # Check if user gets token
        sp = spotipy.Spotify(auth=token)
        user = sp.current_user()
        print user['id']

    return redirect('/musicool/')