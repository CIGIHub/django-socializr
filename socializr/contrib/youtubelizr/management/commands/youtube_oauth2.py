import os

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

from socializr.contrib.youtubelizr.utils import get_creds_path


class Command(BaseCommand):
    help = 'Performs the oauth2 dance and save the creds for future use.'

    def handle(self, *args, **options):
        creds_path = get_creds_path()
        clients_secrets_file = os.path.join(
            creds_path,
            'youtube-client-secret.json',
        )

        storage_file = os.path.join(
            creds_path,
            'youtube-oauth2.json',
        )

        if not os.path.isfile(clients_secrets_file):
            raise ImproperlyConfigured("youtube-client-secret.json not found in {}. Follow instructions in README.md".format(creds_path))

        YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/yt-analytics.readonly"]

        MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

Use APIs Console to generate your youtube-client-secret.json file:
https://code.google.com/apis/console#access

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
"""

        flow = flow_from_clientsecrets(
            clients_secrets_file,
            message=MISSING_CLIENT_SECRETS_MESSAGE,
            scope=" ".join(YOUTUBE_SCOPES),
        )

        storage = Storage(storage_file)
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run(flow, storage)
        else:
            self.stdout.write('YouTube oauth2 is already setup. Delete {} if you want to generate a new token.'.format(storage_file))

