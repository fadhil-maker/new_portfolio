from .base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['django_browser_reload']  # noqa: F405

MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']  # noqa: F405
