
from datetime import datetime, timedelta
import httplib2
import os
import sys
import json

from django.core.exceptions import ImproperlyConfigured

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.tools import run
from optparse import OptionParser


from socializr.base import SocializrConfig, register
from socializr.utils import get_setting
from socializr.contrib.youtubelizr.utils import get_creds_path

from .models import YouTubeChannel, YouTubeAnalytics

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_ANALYTICS_API_SERVICE_NAME = "youtubeAnalytics"
YOUTUBE_ANALYTICS_API_VERSION = "v1"

METRICS = "views,subscribersGained,subscribersLost"
DIMENSIONS = "video"


class YouTubeConfig(SocializrConfig):
    def collect(self):

        storage_file = os.path.join(
            get_creds_path(),
            'youtube-oauth2.json',
        )

        storage = Storage(storage_file)
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            raise ImproperlyConfigured(
                "youtube-oauth2.json not found in {}. Follow instructions in README.md".format(get_creds_path())
            )

        http = credentials.authorize(httplib2.Http())

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=http)

        for channel in YouTubeChannel.objects.all():
            items = youtube.channels().list(
                part="statistics",
                id=channel.channel_id
            ).execute()

            stats = items['items'][0]['statistics']

            YouTubeAnalytics.objects.create(
                channel=channel,
                views=stats[u'viewCount'],
                subscribers=stats[u'subscriberCount'],
                video_count=stats[u'videoCount'],
                date=datetime.now().date(),
            )

