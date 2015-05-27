'''
Main command which is meant to be run daily to get the information
from various social networks into the local db.
'''
import traceback

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured


from socializr.base import get_socializr_configs


class Command(BaseCommand):
    help = 'Performs the oauth2 dance and save the creds for future use.'

    def handle(self, *args, **options):
        configs = get_socializr_configs()

        for config_class in configs:
            config_obj = config_class()
            self.stdout.write("Processing {}".format(config_class.__name__))
            try:
                config_obj.collect()
            except Exception:
                self.stderr.write("There was an exception processing {}".format(config_class.__name__))
                traceback.print_exc()

