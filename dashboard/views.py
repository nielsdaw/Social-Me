import simplejson
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from social_me import services as service
import datetime


@method_decorator(login_required, name='dispatch')
class MainProfileView(TemplateView):
    template_name = "dashboard/main_profile.html"

    def get(self, request, *args, **kwargs):

        facebook = service.check_for_social_media(request, 'facebook')
        instagram = service.check_for_social_media(request, 'instagram')
        linkedin = service.check_for_social_media(request, 'linkedin')
        spotify = service.check_for_social_media(request, 'spotify')

        return render(request, self.template_name, {'user': request.user})


@method_decorator(login_required, name='dispatch')
class SocialMe(TemplateView):
    template_name = "dashboard/social_me.html"
    current_date = datetime.date.today()

    def get(self, request, *args, **kwargs):
        # social media
        social_medias = service.get_social_medias(request)
        data = {}

        # facebook
        facebook = service.check_for_social_media(request, 'facebook')
        facebook_token = facebook['auth_token']
        facebook_places = service.get_tagged_places(facebook_token)
        facebook_likes_locations = service.get_likes_locations(facebook_token)
        facebook_cafes_and_bars = service.get_cafes_and_bars(facebook_token)
        facebook_event_locations = service.get_events_locations(facebook_token)
        facebook_work = service.get_fb_work(facebook_token)
        facebook_education = service.get_fb_education(facebook_token)


        # instagram
        instagram = service.check_for_social_media(request, 'instagram')
        instagram_locations = {}
        if instagram:
            instagram_locations = service.get_media_locations(instagram['access_token'])

        # linkedin
        linkedin = service.check_for_social_media(request, 'linkedin')
        linkedin_imgages = []
        if linkedin:
           linkedin_imgages.append(service.get_flickr_image_linkedin(linkedin['headline']))

        # spotify
        spotify = service.check_for_social_media(request, 'spotify')
        spotify_data = []
        if spotify:
            spotify_data.append(service.get_spotify_artists(spotify['access_token']))
            spotify_data.append(service.get_spotify_tracks(spotify['access_token']))

        return render(request, self.template_name, {'date': self.current_date,
                                                    'social': social_medias,
                                                    'instagram_locations': instagram_locations,
                                                    'facebook_locations': facebook_places,
                                                    'facebook_locations_2': facebook_likes_locations,
                                                    'facebook_locations_3': facebook_event_locations,
                                                    'facebook_cafes': facebook_cafes_and_bars[0],
                                                    'facebook_bars': facebook_cafes_and_bars[1],
                                                    'facebook_work': facebook_work,
                                                    'facebook_education': facebook_education,
                                                    'linkedin_img': linkedin_imgages,
                                                    'spotify_data': spotify_data,
                                                    })


@method_decorator(login_required, name='dispatch')
class FacebookDetailView(TemplateView):
    template_name = "dashboard/facebook_detail.html"

    def get(self, request, *args, **kwargs):

        if 'facebook' in request.session['social_media']:
            return render(request, self.template_name, )
