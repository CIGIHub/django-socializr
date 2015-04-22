import datetime
import collections


from django.core.exceptions import ImproperlyConfigured
from django.utils.timezone import now

try:
    from facepy import GraphAPI
except ImportError as e:
    raise ImproperlyConfigured("Error loading facepy (required by socializr.contrib.facebooklizr): %s" % e)

from socializr.base import SocializrConfig, register
from socializr.utils import get_setting
from .models import FacebookObject, FacebookAnalytics


FACEBOOK_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S+0000'


def fetch_time_data(graph, object_url, value_name):
    ret = {}
    info = graph.get(object_url)
    for data in info['data']:
        if data['period'] != 'day':
            continue
        for value in data['values']:
            date = datetime.datetime.strptime(
                value['end_time'],
                FACEBOOK_DATETIME_FORMAT,
            ).date()
            if date not in ret: ret[date] = {}
            ret[date][value_name] = value['value']

    return ret


def update(d, u):
    for k, v in u.iteritems():
        if isinstance(v, collections.Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d


class FacebookConfig(SocializrConfig):
    def collect(self):
        access_token = get_setting('FACEBOOK_ACCESS_TOKEN', required=True)

        graph = GraphAPI(access_token)

        # Yesterday
        date = (now() - datetime.timedelta(1)).date()

        for object in FacebookObject.objects.all():
            data = {}
            data[date] = {}
            data[date]['page_likes']  = graph.get('/{}/'.format(object.object_id))['likes']

            update(data, fetch_time_data(
                graph,
                '/{}/insights/page_fan_adds_unique/'.format(object.object_id),
                'new_likes',
            ))

            update(data, fetch_time_data(
                graph,
                '/{}/insights/page_posts_impressions/'.format(object.object_id),
                'reach',
            ))

            update(data, fetch_time_data(
                graph,
                '/{}/insights/page_engaged_users/'.format(object.object_id),
                'people_engaged',
            ))


            for date in data:
                analytics, _ = FacebookAnalytics.objects.update_or_create(
                    object = object,
                    date = date,
                    defaults = data[date]
                )


register(FacebookConfig)
