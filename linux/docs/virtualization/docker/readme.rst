###############
docker service
###############

.. contents::

搜索镜像
````````````

这里我们搜索samba镜像

.. code-block::

    docker search samba


查看镜像使用方式
``````````````````

我们通过docker search samba 查找到关于samba的镜像之后，可能却不清楚具体应该如何使用该镜像，所以这里我们访问一个网址

访问：  https://hub.docker.com

然后在这里搜索我们需要的镜像， 比如samba

然后选择一个点进去，就可以看到这个镜像的使用手册了，包括tag。


创建一个容器
``````````````


简单的创建一个centos
----------------------

.. code-block:: bash

    docker run -d -it --name centos centos:6.9


进入到容器里面
```````````````````

docker exec -it centos /bin/bash