import os
from django.conf import settings


def get_creds_path():
    message = 'Setting SOCIALIZR_YOUTUBE_CREDS_PATH must be defined, exist and be a directory.'
    try:
        path = getattr(settings, 'SOCIALIZR_YOUTUBE_CREDS_PATH')
    except AttributeError:
        raise ImproperlyConfigured(message)

    if not os.path.isdir(path):
        raise ImproperlyConfigured(message)

    return path


