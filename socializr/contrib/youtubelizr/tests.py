from django.test import TestCase

from .social import YouTubeConfig
from .models import YouTubeChannel

class YouTubelizrTestCase(TestCase):
    def setUp(self):
        YouTubeChannel.objects.create(
            channel_id = 'UC4SMSzl_jbGe7VFkoOAeRhQ' # CIGI's YouTube channel id
        )

    def test_collect(self):
        yt = YouTubeConfig()
        yt.collect()

