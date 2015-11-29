===============================
Charlesbot Broadcast Message Plugin
===============================

.. image:: https://img.shields.io/travis/marvinpinto/charlesbot-broadcast-message/master.svg?style=flat-square
    :target: https://travis-ci.org/marvinpinto/charlesbot-broadcast-message
    :alt: Travis CI
.. image:: https://img.shields.io/coveralls/marvinpinto/charlesbot-broadcast-message/master.svg?style=flat-square
    :target: https://coveralls.io/github/marvinpinto/charlesbot-broadcast-message?branch=master
    :alt: Code Coverage
.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
    :target: LICENSE.txt
    :alt: Software License

A Charlesbot__ plugin to do a really awesome thing!

__ https://github.com/marvinpinto/charlesbot


How does this work
------------------

This plugin adds the following ``!help`` targets:

.. code:: text
    !command - Do a thing!

TODO: Fill in a description about what this plugin does and how it works.
Screenshots are helpful, too!


Installation
------------

.. code:: bash

    pip install charlesbot-broadcast-message

Instructions for how to run Charlesbot are over at https://github.com/marvinpinto/charlesbot!


Configuration
-------------

In your Charlesbot ``config.yaml``, enable this plugin by adding the following
entry to the ``main`` section:

.. code:: yaml

    main:
      enabled_plugins:
        - 'charlesbot_broadcast_message.broadcastmessage.BroadcastMessage'

TODO: If there is any more configuration, mention it here.

Sample config file
~~~~~~~~~~~~~~~~~~

.. code:: yaml

    main:
      slackbot_token: 'xoxb-1234'
      enabled_plugins:
        - 'charlesbot_broadcast_message.broadcastmessage.BroadcastMessage'


License
-------
See the LICENSE.txt__ file for license rights and limitations (MIT).

__ ./LICENSE.txt
