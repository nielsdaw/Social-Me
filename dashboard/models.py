from django.db import models


class FacebookManager(models.Manager):
    """Manager for the FacebookProfile Model"""

    def create_facebook_profile(
            self,
            facebook_id,
            first_name,
            last_name,
            birthday,
            relationship,
            hometown,
            current_city,
            facebook_email,
            gender,
            profile_picture_url,
            friends_count,
            link,
            age_range,
            last_updated,
            auth_token,
            devices
    ):
        facebook_profile = self.create(
            facebook_id=facebook_id,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            relationship=relationship,
            hometown=hometown,
            current_city=current_city,
            facebook_email=facebook_email,
            gender=gender,
            profile_picture_url=profile_picture_url,
            friends_count=friends_count,
            link=link,
            age_range=age_range,
            last_updated=last_updated,
            auth_token=auth_token,
            devices=devices
        )
        return facebook_profile


class FacebookProfile(models.Model):
    """ FacebookProfile Model, used to store data from the Facebook API """

    facebook_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.TextField(default="")
    relationship = models.TextField(default="")
    hometown = models.TextField(default="")
    current_city = models.TextField(default="")
    facebook_email = models.EmailField(default="")
    gender = models.CharField(max_length=20)
    profile_picture_url = models.TextField(default="")
    friends_count = models.IntegerField(default=0)  # friends['summary']['total_count']
    link = models.TextField(default="")
    age_range = models.IntegerField(default=0)
    last_updated = models.DateTimeField(default="")
    auth_token = models.TextField(default="")
    devices = models.TextField(default="")

    objects = FacebookManager()


class InstagramManager(models.Manager):
    """
        Manager for the InstagramProfil Model
    """

    def create_instagram_profile(
            self,
            instagram_id,
            profile_picture_url,
            bio,
            website,
            username,
            full_name,
            access_token,
            number_of_followers,
            number_of_pictures,
            number_of_following
    ):
        instagram_profile = self.create(
            instagram_id=instagram_id,
            profile_picture_url=profile_picture_url,
            bio=bio,
            website=website,
            username=username,
            full_name=full_name,
            access_token=access_token,
            number_of_followers=number_of_followers,
            number_of_pictures=number_of_pictures,
            number_of_following=number_of_following
        )
        return instagram_profile


class InstagramProfile(models.Model):
    """
        InstagramProfile Model, used to store data from the Instagram API
    """

    instagram_id = models.IntegerField(default=0)
    profile_picture_url = models.TextField(default="")
    bio = models.TextField(default="")
    website = models.CharField(default="", max_length=100)
    username = models.CharField(default="", max_length=255)
    full_name = models.CharField(default="", max_length=255)
    access_token = models.TextField(default="")
    number_of_followers = models.IntegerField(default=0)
    number_of_pictures = models.IntegerField(default=0)
    number_of_following = models.IntegerField(default=0)

    objects = InstagramManager()


class LinkedinManager(models.Manager):
    """
        Manager for the LinkedinProfile Model
    """

    def create_linkedin_profile(
            self,
            first_name,
            last_name,
            email,
            headline,
            industry,
            location,
            recent_shared,
            number_of_connections,
            summary,
            specialities,
            current_position,
            profile_picture_url
    ):
        linkedin_profile = self.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            headline=headline,
            industry=industry,
            location=location,
            recent_shared=recent_shared,
            number_of_connections=number_of_connections,
            summary=summary,
            specialities=specialities,
            current_position=current_position,
            profile_picture_url=profile_picture_url
        )
        return linkedin_profile


class LinkedinProfile(models.Model):
    """
        LinkedIn Profile Model, used to store data from the LinkedIn API
    """
    first_name = models.CharField(default="", max_length=255)
    last_name = models.CharField(default="", max_length=255)
    email = models.EmailField(default="")
    headline = models.TextField(default="")
    industry = models.TextField(default="")
    location = models.TextField(default="")
    recent_shared = models.TextField(default="")
    number_of_connections = models.IntegerField(default=0)
    summary = models.TextField(default="")
    specialities = models.TextField(default="")
    current_position = models.TextField(default="")
    profile_picture_url = models.TextField(default="")

    objects = LinkedinManager()


class SpotifyManager(models.Manager):
    """
        Manager for the SpotifyProfile Model
    """

    def create_spotify_profile(
            self,
            display_name,
            email,
            followers,
            access_token,
            profile_picture_url,
    ):
        spotify_profile = self.create(
            display_name=display_name,
            email = email,
            followers = followers,
            access_token = access_token,
            profile_picture_url = profile_picture_url
        )

        return spotify_profile


class SpotifyProfile(models.Model):
    """
        Spotify Profile Model, used to store data from the LinkedIn API
    """
    display_name = models.CharField(default="", max_length=255)
    email = models.EmailField(default="")
    followers = models.TextField(default="")
    access_token = models.TextField(default="")
    profile_picture_url = models.TextField(default="")

    objects = SpotifyManager()


class TwitterProfile(models.Model):
    # TODO create this model - Twitter
    pass


class SoundCloudProfile(models.Model):
    # TODO create this model - SoundCLoud
    pass