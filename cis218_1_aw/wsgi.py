"""
Aaron Whitaker
CIS218 - Web Application Programming
9/22/2022
"""

"""
WSGI config for cis218_1_aw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cis218_1_aw.settings')

application = get_wsgi_application()
