from django.test import TestCase

from .social import FacebookConfig
from .models import FacebookObject, FacebookAnalytics

class FacebooklizrTestCase(TestCase):
    def setUp(self):
        FacebookObject.objects.create(
            object_id = '100911698621' # CIGI's Facebook page
        )

    def test_collect(self):
        f = FacebookConfig()
        f.collect()

        for analytics in FacebookAnalytics.objects.all():
            print(analytics.__dict__)
