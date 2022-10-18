"""
Aaron Whitaker
CIS218 - Web Application Programming
9/22/2022
"""

"""
ASGI config for cis218_1_aw project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cis218_1_aw.settings')

application = get_asgi_application()
