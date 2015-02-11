__author__ = 'evanwu'
import os
import subprocess
from spotipy import oauth2
import spotipy
import pprint

def prompt_user_login(username=''):

    scope = 'user-library-read'
    client_id = '38d99462b8514ed28c8a1629381d84c6'
    client_secret = 'ded9f53ab7144273bb5ef656b2b6cc50'
    redirect_uri = 'http://127.0.0.1:8000/musicool/spotify_login/'
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope, cache_path=".cache-" + username)

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:

        auth_url = sp_oauth.get_authorize_url()

        try:
            subprocess.call(["open", auth_url])
            print "Opening %s in your browser" % auth_url

        except:
            print "Please navigate here: %s" % auth_url



def exchange_token_with_code(code=None, username=''):

    scope = 'user-library-read'
    client_id = '38d99462b8514ed28c8a1629381d84c6'
    client_secret = 'ded9f53ab7144273bb5ef656b2b6cc50'
    redirect_uri = 'http://127.0.0.1:8000/musicool/spotify_login/'
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope, cache_path=".cache-" + username)

    token_info = sp_oauth.get_cached_token()

    if token_info:  # Found token in cache
        return token_info['access_token']
    else:  # Can't find cache token, exchange one with code
        if code:
            token_info = sp_oauth.get_access_token(code)
            # Auth'ed API request
            if token_info:
                return token_info['access_token']
            else:
                return None
        else:
            print 'Something wrong!'


def search_spotify_helper(search_str=''):

    sp = spotipy.Spotify()
    result = sp.search(search_str)
    pprint.pprint(result)