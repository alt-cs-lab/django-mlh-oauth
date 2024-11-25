import os
from django.conf import settings

DEFAULT_OAUTH_SETTINGS = {
    'CAS_SERVER_URL': 'https://signin.k-state.edu/WebISO/',
    'CAS_LOGOUT_COMPLETELY': True,
    'CAS_REDIRECT_URL': '/authed/' if os.environ.get('CODESPACES') is None else 'https://' + os.environ.get('CODESPACE_NAME') + '-8000.' + os.environ.get('GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN') + '/authed/',
    'LOGIN_URL': '/accounts/login/',
    'LOGOUT_URL': '/accounts/logout/',
}

for key, value in DEFAULT_OAUTH_SETTINGS.items():
    setattr(settings, key, getattr(settings, key, value))

settings.MIDDLEWARE = getattr(settings, 'MIDDLEWARE', []) + [
   'allauth.account.middleware.AccountMiddleware',
]
settings.AUTHENTICATION_BACKENDS = getattr(settings, 'AUTHENTICATION_BACKENDS', []) + [
    'allauth.account.auth_backends.AuthenticationBackend',
]