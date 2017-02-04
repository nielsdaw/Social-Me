# -*- coding: utf-8 -*-
import six

from django.conf import settings
from django.contrib import messages
from django.contrib.messages.api import MessageFailure
from django.shortcuts import redirect
from django.utils.http import urlquote
from social.exceptions import SocialAuthBaseException
from social.utils import social_logger
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(SocialAuthExceptionMiddleware):

    def process_exception(self, request, exception):
        auth_unexpected = 'An unexpected error occurred, please try to connect again!'
        auth_associated = 'The {} account you are trying to connect is already used by someone else. Please try again!'
        auth_cancel = 'You cancelled the connection to {}. Please try again!'
        url = self.get_redirect_uri(request, exception)

        if isinstance(exception, SocialAuthBaseException):
            backend = getattr(request, 'backend', None)
            backend_name = getattr(backend, 'name', 'unknown-backend')

            if type(exception) == social_exceptions.AuthAlreadyAssociated:
                messages.add_message(request, messages.INFO, auth_associated.format(backend_name))
            elif type(exception) == social_exceptions.AuthCanceled:
                messages.add_message(request, messages.INFO, auth_cancel.format(backend_name))
            else:
                messages.add_message(request, messages.INFO, auth_unexpected)
        
        print("AuthException: {}".format(exception))
        return redirect(url)







class SocialAuthExceptionMiddlewareCustom(MiddlewareMixin):
    """Middleware that handles Social Auth AuthExceptions by providing the user
    with a message, logging an error, and redirecting to some next location.

    By default, the exception message itself is sent to the user and they are
    redirected to the location specified in the SOCIAL_AUTH_LOGIN_ERROR_URL
    setting.

    This middleware can be extended by overriding the get_message or
    get_redirect_uri methods, which each accept request and exception.
    """
    def process_exception(self, request, exception):
        strategy = getattr(request, 'social_strategy', None)
        if strategy is None or self.raise_exception(request, exception):
            return

        if isinstance(exception, SocialAuthBaseException):
            backend = getattr(request, 'backend', None)
            backend_name = getattr(backend, 'name', 'unknown-backend')

            message = self.get_message(request, exception)
            social_logger.error(message)

            url = self.get_redirect_uri(request, exception)
            try:
                messages.error(request, message,
                               extra_tags='social-auth ' + backend_name)
            except MessageFailure:
                url += ('?' in url and '&' or '?') + \
                       'message={0}&backend={1}'.format(urlquote(message),
                                                        backend_name)
            return redirect(url)

    def raise_exception(self, request, exception):
        strategy = getattr(request, 'social_strategy', None)
        if strategy is not None:
            return strategy.setting('RAISE_EXCEPTIONS', settings.DEBUG)

    def get_message(self, request, exception):
        return six.text_type(exception)

    def get_redirect_uri(self, request, exception):
        strategy = getattr(request, 'social_strategy', None)
        return strategy.setting('LOGIN_ERROR_URL')





