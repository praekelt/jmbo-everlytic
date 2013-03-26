from xmlrpclib import ServerProxy, Fault, Error, ProtocolError
from xml.parsers.expat import ExpatError

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


def subscribeUser(last_name, first_name, 
                  email, receive_email,
                  everlytic_id):
    """ Subscribe the user to the everlytic mailing list, and return the
    everlytic user id to the caller.
    """
    # create the connection to the host
    sp = None
    try:
        sp = ServerProxy(EVERLYTIC_HOST)
    except IOError:
        return -1

    # Check for an existing everlytic user just to be safe
    if everlytic_id == 0:
        everlytic_id = _checkForExistingEverlyticUser(last_name,
                                                     first_name,
                                                     email, sp)

    if everlytic_id < 0:
        # We have a new Everlytic user, so create the user on the everlytic
        # database, even if they don't subscribe to mailing lists yet.
        return _createEverlyticUser(sp, email, receive_email,
                                    last_name, first_name)

    # For an existing user, update her status on the list
    return _createEverlyticUser(sp, email, receive_email)


def _createEverlyticUser(sp, email, receive_email, 
                         last_name=None, first_name=None):
    """ Create a new user on the EverLytic service and (un)subscribe them to
    the list, all in one go.
    """
    params = {
            'contact_email': email
            }
    if first_name is not None:
        params['contact_name'] = first_name
    if last_name is not None:
        params['contact_lastname'] = last_name
    try:
        result = sp.contacts.create(EVERLYTIC_API_KEY, 
                params, 
                [EVERLYTIC_LIST_ID], 
                receive_email and "subscribed" or "unsubscribed", 
                "update")
        if result['status'] == 'success':
            return result['contact_id']
        else:
            # TODO: Log the result['message']
            pass
    except Fault:
        # TODO: Log the error
        pass
    return -1


def _checkForExistingEverlyticUser(last_name, first_name, email, sp):
    """ Check if the user exists on the Everlytic database
    """
    try:
        # see if the user exists on the EverLytic service
        result = sp.contacts.getBatch(EVERLYTIC_API_KEY, {
            'contact_lastname': last_name,
            'contact_name': first_name,
            'contact_email': email
            })
        if int(result['total']) > 0:
            # TODO: Make sure this compromise will work!
            # Take the first result in the returned list
            everlytic_user = result['data'][0]
            return everlytic_user['contact_id']
    except Fault:
        # TODO: Log the error
        pass
    except ExpatError:
        pass
    return -1


def deleteEverlyticUser(contact_id):
    """ Delete the given contact from the Everlytic database
    """
    # create the connection to the host
    sp = None
    try:
        sp = ServerProxy(EVERLYTIC_HOST)
    except IOError:
        # TODO: Log the error
        return
    try:
        result = sp.contacts.delete(EVERLYTIC_API_KEY, contact_id)
        if result['status'] != 'success':
            # TODO: LOG the result['message']
            pass
    except Fault:
        # TODO: Log the error
        pass
    except ExpatError:
        pass
