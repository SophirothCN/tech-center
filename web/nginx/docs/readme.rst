
nginx
#####################

.. contents::

ubuntu14 upgrade nginx
-----------------------------------


.. code-block:: bash

    echo deb http://nginx.org/packages/ubuntu/ trusty nginx >> /etc/apt/sources.list
    echo deb-src http://nginx.org/packages/ubuntu/ trusty nginx >> /etc/apt/sources.list
    apt-get update
    apt-get upgrade nginx