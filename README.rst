teleport-client
===============

Watches for filesystem changes and communicates with the teleport API to synchronize the changes to the server.

For the server-side API, see django-teleport_.

It watches for filesystem changes using the amazing library called watchdog_.

.. _django-teleport: https://github.com/dash1291/django-teleport
.. _watchdog: https://github.com/gorakhargosh/watchdog

Installation
-------------

You need to grab the copy of the source code.

You can either clone the repository, using:

``git clone https://github.com/dash1291/teleport-client.git``

Or, you can also download the source code as a zip file and extract the code into a directory.

Configuation
------------

To get the client working, you need to create a file ``config.py`` in the source code directory, with the following contents.

.. code-block:: python

    API_BASE_URI = "http://localhost:8000"   # This should point to the url of the teleport server.
    API_SECRET = "api secret as configured on the server"
    PATH_PREFIX = "Absolute path of the local folder to synchronize"
