teleport-client
===============

Watches for filesystem changes and communicates with the teleport API to synchronize the changes to the server.

For the server-side API, see django-teleport_.

It watches for filesystem changes using the amazing library called watchdog_.

.. _django-teleport: https://github.com/dash1291/django-teleport
.. _watchdog: https://github.com/gorakhargosh/watchdog