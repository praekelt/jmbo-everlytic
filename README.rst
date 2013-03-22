jmbo-everlytic
==============

jmbo-everlytic provides integration with the everlytic (pMailer) API.
The only functionality supported is adding an removing members from a
mailing list subscription.

The communication protocol with the everlytic service is xmlrpc.

Requirements
------------

System libraries
****************
- libxml2-dev

Python packages
***************
- xmlrpclib

Usage
-----

`everlytic.api` contains functions for subscribing and unsubscribing to a
mailing list. A local everlytic profile is stored to keep track of the
member id on everlytic.

Settings
********
The following settings must be added to settings.py:
::
    ERVERLYTIC = {
        'URL': 'http://praekelt-host2.pmailer.net/api/1.0'
        'USERNAME': 'xxxxx',
        'PASSWORD': 'xxxxx',
        'API_KEY': 'DwnGAw4ISfcqLmqnGRYrXOeJw8L3eJBS',
        'LIST_ID': '12701 - ECR Subscriptions' 
    }
::
