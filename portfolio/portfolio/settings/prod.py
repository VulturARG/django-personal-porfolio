from .base import *

DEBUG = True

# load production server from .env
<<<<<<< HEAD
ALLOWED_HOSTS = ['localhost', '127.0.0.1',os.getenv('SERVER', default='127.0.0.1'),'django']
#ALLOWED_HOSTS = ['*']
=======
#ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]
ALLOWED_HOSTS = ['localhost', '127.0.0.1',os.getenv('SERVER', default='127.0.0.1'),'django','luis.briones.com.ar']
#ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
    'tinymce',
]
>>>>>>> bd26d0e4e132b5a4273dce28eb270cdf75b62b6d

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

<<<<<<< HEAD
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
=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db_postgres',
        'PORT': 5432
>>>>>>> bd26d0e4e132b5a4273dce28eb270cdf75b62b6d
    }
}
