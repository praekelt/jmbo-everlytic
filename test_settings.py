DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'skeleton.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': 'everlytic_test',
    }
}

# A tuple of callables that are used to populate the context in RequestContext. 
# These callables take a request object as their argument and return a 
# dictionary of items to be merged into the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'preferences.context_processors.preferences_cp',
    'foundry.context_processors.foundry',
)

FOUNDRY = {
    'layers': ('basic', )
}

# AppDirectoriesTypeLoader must be after filesystem loader
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'foundry.loaders.AppDirectoriesTypeLoader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = [
    'atlas',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.gis',
    'django.contrib.sessions',
    'category',
    'preferences',
    'jmbo',
    'competition',
    'photologue',
    'secretballot',
    'publisher',
    'foundry',
    'everlytic',
    'compressor',
    'social_auth'
]

EVERLYTIC = {
    'URL': 'http://praekelt-host2.pmailer.net/api/1.0',
    'API_KEY': 'DwnGAw4ISfcqLmqnGRYrXOeJw8L3eJBS',
    'LIST_ID': 12701    # ECR Subscriptions
}

STATIC_URL = 'static/'

SITE_ID = 1
