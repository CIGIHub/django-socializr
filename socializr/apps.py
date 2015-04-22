from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SocializrConfig(AppConfig):
    """Default AppConfig which does autodiscovery"""
    name = 'socializr'

    def ready(self):
        self.module.autodiscover()

