from .middleware_settings import *  # noqa: ignore=F401 isort:skip
from .installed_apps_settings import *  # noqa: ignore=F401 isort:skip
from .internationalizations_settings import *  # noqa: ignore=F401 isort:skip
from .auth_settings import *  # noqa: ignore=F401 isort:skip
from .host_settings import *  # noqa: ignore=F401 isort:skip
from .media_settings import *  # noqa: ignore=F401 isort:skip
from .email_settings import *  # noqa: ignore=F401 isort:skip
from .database_settings import *  # noqa: ignore=F401 isort:skip
from .rest_settings import *  # noqa: ignore=F401 isort:skip
from .new_api_settings import *  # noqa: ignore=F401 isort:skip

from pathlib import Path

SECRET_KEY = 'django-insecure-nh75ao&dcno%3pu!4xcs-u-l0#)y-db@n67xh$^%#r@rpwu@4='

DEBUG = True

DJANGO_SETTINGS_MODULE = 'app_api.settings.base'

ROOT_URLCONF = 'app_api.urls'

WSGI_APPLICATION = 'app_api.wsgi.application'

# CSRF_FAILURE_VIEW = 'core.views_errors.csrf_failure'
