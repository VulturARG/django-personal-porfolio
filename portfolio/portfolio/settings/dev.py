from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'tinymce',
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]