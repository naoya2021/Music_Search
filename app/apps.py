from django.apps import AppConfig
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
