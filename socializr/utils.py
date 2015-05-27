
import os
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def get_setting(name, required=False):
    '''
    Precedence: environment variables, django settings
    '''
    name = 'SOCIALIZR_{}'.format(name)

    value = os.environ.get(name)

    if value is not None:
        return value

    if hasattr(settings, name):
        return getattr(settings, name)

    if required:
        raise ImproperlyConfigured(
            'Setting {} is required to be set either in the environment or settings.py'.format(name)
        )

    return None
