"""
WSGI config for instagram_tool_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
import django

#from django.core.wsgi import get_wsgi_application

path = '/srv/sites/instagram_tool_project'
if path not in sys.path:
    sys.path.append(path)
sys.path.append('/srv/envs/iskandre_env/lib/python3.5/site-packages')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram_tool_project.settings")

application = get_wsgi_application()
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()