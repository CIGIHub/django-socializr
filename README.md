# django-socializr

Django app used to aggregate social data.

Requires Django 1.7 or newer since it uses the AppConfig framework.

## Contrib

Generally settings can either be in the enivronment or set in
settings.py

### contrib.facebooklizr

Requirements: `facepy`

Settings:

* SOCIALIZR_FACEBOOK_ACCESS_TOKEN

### contrib.youtublizr

Requirements:

* `google-api-python-client`
* `python-gflags'

Settings:

* SOCIALIZR_YOUTUBE_CREDS_PATH (suggested: os.path.join(BASE_DIR, 'creds'))

#### OAuth2 Dance

Where to be begin...

The goal is a file which stores your bearer token for oauth2. To get it
you will need to:

* Create a project under googles [API interface].(https://code.google.com/apis/console#:access)
* Create a new Client ID (type Installed Application)
* Download the .json file and save it in SOCIALIZR_YOUTUBE_CREDS_PATH as
  `youtube-client-secret.json`
* run the command `python manage.py youtube_oauth2`
* This will open a browser when you will have to sign in your username
  and password.
* The result will save the creds to disk under the SOCIALIZR_YOUTUBE_CREDS_PATH

You should be able to deploy the genereated youtube-oauth2.json file to
the product server for reuse.

The token lifetime is until is revoked by the user.



