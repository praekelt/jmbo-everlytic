from foundry.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'test_everlytic.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS += ('everlytic',)

EVERLYTIC = {
    'URL': 'http://your-host.pmailer.net/api/1.0',
    'API_KEY': 'your_api_key',
    'LIST_ID': 0
}
