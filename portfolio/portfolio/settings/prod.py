from .base import *

DEBUG = False

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1',os.getenv('SERVER', default='127.0.0.1'),'django']
#ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'db_postgres',
#         'PORT': 5432
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
