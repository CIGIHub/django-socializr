
from django.utils.module_loading import autodiscover_modules

from . import base


def autodiscover():
    autodiscover_modules('social', register_to=base)


default_app_config = 'socializr.apps.SocializrConfig'
