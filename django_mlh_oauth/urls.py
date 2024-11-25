from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from django_mlh_oauth.provider import MLHProvider

urlpatterns = default_urlpatterns(MLHProvider)