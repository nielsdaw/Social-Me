from django.shortcuts import render
from restless.views import Endpoint
from social_me import services
from restless.auth import BasicHttpAuthMixin, login_required
from restless.models import serialize


class HelloWorld(Endpoint, BasicHttpAuthMixin):
    def get(self, request):
        print("sm; {}".format(services.get_social_medias(request)))
        name = request.params.get('name', 'World')
        return {'message': 'Hello, %s!' % name}


class FacebookLikesLocations(Endpoint):
    def get(self, request):
        facebook = services.check_for_social_media(request, 'facebook')
        facebook_token = facebook['auth_token']
        facebook_likes_locations = services.get_likes_locations(facebook_token)

        return serialize(facebook_likes_locations)


class FacebookEventsLocations(Endpoint):
    def get(self, request):
        facebook = services.check_for_social_media(request, 'facebook')
        facebook_token = facebook['auth_token']
        facebook_event_locations = services.get_events_locations(facebook_token)


class FacebookTaggedLocations(Endpoint):
    def get(self, request):
        facebook = services.check_for_social_media(request, 'facebook')
        facebook_token = facebook['auth_token']
        facebook_places = services.get_tagged_places(facebook_token)