import os
import sys

path='/srv/sites/instagram_tool_project'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'instagram_tool_project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()