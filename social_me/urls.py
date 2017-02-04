"""digital_identity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = [
    url(
        r"login/$",
        views.LoginView.as_view(),
        name="login"
    ),
    url(
        r"logout/$",
        views.LogoutView.as_view(),
        name="logout"
    ),
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    url(
        r'^connect/',
        views.HomePageView.as_view(),
        name='connect'
    ),
    url(
        r'^privacy_policy/',
        views.PrivacyPolicyView.as_view(),
        name='privacy_policy'
    ),
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^dashboard/',
        include('dashboard.urls', namespace='dashboard')
    ),
    url(r'api/',
        include('api.urls', namespace='api')
        ),
    url(
        '',
        include('social.apps.django_app.urls', namespace='social')
    ),
    url(
        '',
        include('django.contrib.auth.urls', namespace='auth')
    ),
]
