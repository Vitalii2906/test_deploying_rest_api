import os
import sys

from django.core.wsgi import get_wsgi_application

path = '/home/GuruWithYou/myproject'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

application = get_wsgi_application()
