from xmlrpclib import ServerProxy, Fault, Error, ProtocolError

from django.conf import settings


try:
    CONFIG = getattr(settings, 'EVERLYTIC')
    EVERLYTIC_HOST = CONFIG['URL']
    EVERLYTIC_API_KEY = CONFIG['API_KEY']
    EVERLYTIC_LIST_ID = CONFIG['LIST_ID']
except AttributeError:
    raise exceptions.ImproperlyConfigured("EVERLYTIC settings are missing")
except KeyError as e:
    raise exceptions.ImproperlyConfigured(
            "EVERLYTIC setting %s is missing." % str(e))

