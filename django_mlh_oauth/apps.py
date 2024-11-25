from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    name = 'django_mlh_oauth'
    WEB_URL = 'https://my.mlh.io'
    API_URL = '{0}/api/v3'.format(WEB_URL)
