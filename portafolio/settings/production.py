from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': config('DB_NAME_'),
        'USER': config('DB_USER_'),
        'PASSWORD': config('DB_PASSWORD_'),
        'HOST': config('DB_HOST_'),
        'PORT': config('DB_PORT_'),
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'