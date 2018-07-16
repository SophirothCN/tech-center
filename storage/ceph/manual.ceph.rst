ceph manual
##################

.. contents::


rdb创建一个块设备
`````````````````````

.. code-block:: bash

    rbd create test1 --image-format 1 --size 5G

查看块设备列表
```````````````````

.. code-block:: bash

    rbd ls

查看指定块设备的信息
```````````````````````
这里我们有一个块设备的名称叫做test1,我们来查看它的信息。

.. code-block:: bash

    rbd info test1


rbd映射
````````````````
这里我们讲test1映射为rbd0了，
.. code-block:: bash

    rbd map test1
    lsblk
    ls -l /dev/rbd0
    rbd showmapped



ceph创建pool
``````````````````

.. code-block:: bash

    ceph osd pool create volumes 64
    ceph osd pool create images 64
    ceph osd pool create vms 64

查看pool的列表
``````````````````````

.. code-block:: bash

    ceph osd pool ls


查看pool的状态
```````````````````
这里我们可以查看所有pool的状态，也可以指定pool名查看指定pool的状态

.. code-block:: bash

    ceph osd pool stats
    ceph osd pool stats vms

ceph客户端软件安装
```````````````````````

.. code-block:: bash

    yum install python-rbd ceph-common  -y


创建ceph用户和密钥
`````````````````````

.. code-block:: bash

    ceph auth get-or-create client.cinder mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=volumes, allow rwx pool=vms, allow rx pool=images'
    ceph auth get-or-create client.glance mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=images'
    ceph auth get-or-create client.cinder-backup mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=backups'


ceph 用户验证列表
```````````````````````

.. code-block:: bash

    ceph auth list