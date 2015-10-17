"""
WSGI config for wysadzulice_pl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

activate_this = '/root/.virtualenvs/wysadzulice_pl/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from django.core.wsgi import get_wsgi_application  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wysadzulice_pl.settings")

application = get_wsgi_application()
