from xmlrpclib import ServerProxy, Fault, Error, ProtocolError

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


try:
    EVERLYTIC_HOST = settings.EVERLYTIC['URL']
    EVERLYTIC_API_KEY = settings.EVERLYTIC['API_KEY']
    EVERLYTIC_LIST_ID = settings.EVERLYTIC['LIST_ID']
except AttributeError:
    raise ImproperlyConfigured("EVERLYTIC settings are missing")
except KeyError as e:
    raise ImproperlyConfigured("EVERLYTIC setting %s is missing." % str(e))


def subscribeUser(user):
    """ Subscribe the user to the everlytic mailing list, and return the
    everlytic user id to the caller.
    """
    return 200


def unsubscribeUser(user):
    """ unsubscribe the user from the Everlytic mailing list.
    """
    pass
