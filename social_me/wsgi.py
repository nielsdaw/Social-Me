"""
WSGI config for digital_identity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import logging

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

path = "/Users/nielsdaw/PycharmProjects/social_me/"
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_me.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)-8s %(message)s",
)

# #-- Settings local
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_me.settings")
#
# application = get_wsgi_application()
