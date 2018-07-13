system monitor commands
#############################

.. contents::

找出系统中使用CPU最多前5个进程？
``````````````````````````````
.. code-block:: bash

    ps -eo pcpu,pid,cmd|sort -nr|head -5

