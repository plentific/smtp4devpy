========
SMTP4DEV
========

An abstraction library to access the messages captured by an
_SMTP4dev instance.

.. _SMTP4dev: https://github.com/rnwood/smtp4dev/


------------
Installation
------------

Install with pip::

  pip install smtp4dev


-----
Usage
-----

Example usage::

  from smtp4dev import Smtp4Dev
  m = client.get_message(a[0].pk)
  client = Smtp4Dev('http://localhost:8080')
  a = list(client.list_messages())
  m = client.get_message(a[0].pk)
