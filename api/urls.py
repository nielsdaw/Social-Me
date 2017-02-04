from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$',
        views.HelloWorld.as_view()
        ),
    url(r'facebook/likes/locations$',
        views.FacebookLikesLocations.as_view(), name="likes"
        ),
]


