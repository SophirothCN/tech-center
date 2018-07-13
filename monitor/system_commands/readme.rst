linux common monitor commands
#############################

.. contents::

找出系统中使用CPU最多前5个进程？
``````````````````````````````
.. code-block:: bash

    ps -eo pcpu,pid,cmd|sort -nr|head -5

找出系统中使用内存最多的五个进程？

.. code-block:: bash

ps -eo rss,pid,cmd|sort -nr|head -5


只显示有磁盘io的进程,以千字节显示,非交互式显示，显示三次
`````````````````````````````````````````````````````````

.. code-block:: bash

    iotop -P -k -o -b -n3

找出系统中使用网络最多的进程？
```````````````````````````````

.. code-block:: bash

    iftop