find
##############

.. contents::


查看指定目录内两分钟内有修改的文件
``````````````````````````````````````
.. code-block::

    find /var/log -cmin -2


查看指定目录内命名为指定名称的文件
``````````````````````````````````````````
.. code-block::

    find . -name original-ks.cfg

支持通配符,使用通配符的是要要加引号。

.. code-block::

    find /var/log/ -name '*.log'


要忽略 a 目录：
```````````````````
.. code-block:: bash

    find . -path ./a -prune -o -type f -name s.txt -print