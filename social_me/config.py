

# -- Social Auth Settings --


# used social backends

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.instagram.InstagramOAuth2',
    'social.backends.linkedin.LinkedinOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.spotify.SpotifyOAuth2',
)



# Custom namespace

SOCIAL_AUTH_URL_NAMESPACE = 'social'


# Redirects


# Used to redirect the user once the auth process ended successfully.
# The value of ?next=/foo is used if it was present
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/connect/'

# URL where the user will be redirected in case of an error
SOCIAL_AUTH_LOGIN_ERROR_URL = '/connect/'


# Used to redirect new registered users, will be used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL if defined.
# Note that ?next=/foo is appended if present, if you want new users to go to next, you’ll need to do it yourself.
# -SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'

# Like SOCIAL_AUTH_NEW_USER_REDIRECT_URL but for new associated accounts (user is already logged in).
# Used in place of SOCIAL_AUTH_LOGIN_REDIRECT_URL
# -SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'

# The user will be redirected to this URL when a social account is disconnected
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/logout/'

# Inactive users can be redirected to this URL when trying to authenticate.
# -SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'


# Add to pipeline

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social_me.pipeline.update_profile',
)

# pipeline session fields

FIELDS_STORED_IN_SESSION = ['linkedin', ]


# Profile model

AUTH_PROFILE_MODULE = 'django.contrib.auth.models.User'



# -- backend settings ---


# Instagram auth

SOCIAL_AUTH_INSTAGRAM_KEY = ''

SOCIAL_AUTH_INSTAGRAM_SECRET = ''

SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {
    'scope':
        'basic'
}



# --- NO FIELDS FOR INSTAGRAM, ONLY SCOPE ---



# facebook auth

SOCIAL_AUTH_FACEBOOK_KEY = ''

SOCIAL_AUTH_FACEBOOK_SECRET = ''

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'public_profile',
    'email',
    'user_friends',
    'user_birthday',
    'user_relationships',
    'user_hometown',
    'user_tagged_places',
    'user_location',
    'user_likes',
    'user_events',
    'user_work_history',
    'user_education_history'
]



SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id,'
            'name,'
            'first_name,'
            'last_name,'
            'picture,'
            'email,'
            'age_range,'
            'link,'
            'gender,'
            'locale,'
            'timezone,'
            'updated_time,'
            'friends,'
            'about,'
            'birthday,'
            'devices,'
            'relationship_status,'
            'hometown,'
            'location'
}


# LinkedIn settings

SOCIAL_AUTH_LINKEDIN_KEY = ''

SOCIAL_AUTH_LINKEDIN_SECRET = ''

SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile','r_emailaddress']

SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
    'email-address',
    'headline',
    'industry',
    'location',
    'current-share',
    'num-connections',
    'num-connections-capped',
    'summary',
    'specialties',
    'positions',
    'picture-url',
    'picture-urls::(original)',
]


# --- Spotify settings ---

SOCIAL_AUTH_SPOTIFY_KEY = ''

SOCIAL_AUTH_SPOTIFY_SECRET = ''

SOCIAL_AUTH_SPOTIFY_SCOPE = ['user-top-read', 'user-read-email','user-read-birthdate']



