# coding=utf-8
import os, socket
from .base import BASE_DIR

YANDEX_MAPS_API_KEY = 'AO7kF1UBAAAA-akFCwIAR7_VYsSjwJ9g-dDEVHElLxuBQi8AAAAAAAAAAAAQMK4N7NYtvg4ALgMZ8-GRO_cQqQ=='
HTMLWEB_API_KEY = '6b0fc55b1628dd1c05b5b386b5f45f35'


if socket.gethostname() == 'r420':
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'enjoyafrru_lead',
             'USER': 'leader',
             'PASSWORD': '1111',
             'HOST': 'localhost',
             'PORT': '',
         }
    }
else:
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'enjoyafrru2_lead',
             'USER': 'enjoyafrru2_lead',
             'PASSWORD': 'alena2010',
             'HOST': 'localhost',
             'PORT': '',
         }
    }

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'width': 700,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['FontSize', 'TextColor'],
            ['Bold', 'Italic', 'Underline'],
            ['Table', 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image'],
            ['RemoveFormat', 'Source']
        ]
    },
}
