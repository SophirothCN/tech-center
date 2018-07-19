nginx 转发tcp
#####################


.. contents::

Description
---------------------

Nginx 转发tcp端口需要使用到**stream** 这个模块，至少要nginx1.9以上的版本才有这个功能，所以使用前请先确认你的版本是nginx1.9以上的。




Configuration
-------------------

这里我们在nginx的nginx.conf里配置如下的内容，就可以将本服务器的3389端口转发到192.168.0.234的3389端口了。 3389是我们windows服务器的远程桌面端口。

.. code-block:: bash

    stream {
        upstream bi_remote_desk {
            server 192.168.0.234:3389;
        }
        server {
            listen 3389; ##监听端口
            proxy_pass bi_remote_desk;  #转发请求
        }

    }
