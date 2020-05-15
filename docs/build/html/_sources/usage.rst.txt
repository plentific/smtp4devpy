Usage
=====

A brief introduction to the basic usage of the library.
See the API documentation for more details.

Client
^^^^^^

All API connectivity is abstracted behind a client. This
allows listing and retrieval of emails. Example::

    from smtp4dev import Smtp4Dev
    client = Smtp4Dev('http://localhost:8080')
    messages = client.list_messages()


Message
^^^^^^^

*Message* is the abstraction of an Email. They contain the
following properties:

- sender
- recipients
- received_date
- subject
- body


Example usage
^^^^^^^^^^^^^

::

    from smtp4dev import Smtp4Dev
    client = Smtp4Dev('http://localhost:8080')
    messages = client.list_messages()
    
    for message in messages:
        print("from {}: {}".format(message.sender, message.subject))
