openstack manual
######################


.. contents::

引用openstack管理变量
`````````````````````````

.. code-block:: bash

    source ./admin-openstack.sh

查看openstack内相关信息
````````````````````````````
endpoint 列表
---------------------

.. code-block:: bash

    openstack endpoint list

查看指定服务endpoint列表
----------------------------
.. code-block:: bash

    openstack endpoint list --service nova


网络相关
---------------

查看网络代理列表
++++++++++++++++++++++++

.. code-block:: bash

    openstack network agent list


查看子网
++++++++++++++++++++++++

.. code-block:: bash

    openstack subnet list

查看网络
++++++++++++++++
.. code-block:: bash

    openstack network list
    # neutron net-list
    # neutron subnet-list

计算相关
---------------



查看节点
+++++++++++++++++++++
.. code-block:: bash

    nova service-list
    openstack catalog list
    nova-status upgrade check

查看计算服务列表
+++++++++++++++++++++

.. code-block:: bash

    openstack compute service list


查看虚拟机实例列表
+++++++++++++++++++++
.. code-block:: bash

    openstack server list

查看虚拟控制台访问实例url
+++++++++++++++++++++

这里我们查看虚拟机kvm01-cirros的vnc地址

.. code-block:: bash

    openstack console url show kvm01-cirros

安全相关
-----------------

可用的安全组列表
+++++++++++++++++++++++
.. code-block:: bash

    openstack security group list

创建秘钥
+++++++++++++++++++++++
.. code-block:: bash

    ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
    nova keypair-add --pub-key ~/.ssh/id_dsa.pub mykey
    nova keypair-list #查看密钥

资源相关
-------------------

云主机可用类型
++++++++++++++++++++++
.. code-block:: bash

    openstack flavor list

镜像列表
++++++++++++++
.. code-block:: bash

    openstack image list



创建openstack相关信息
```````````````````````````

创建可用域(Zone计算节点集合)
------------------------------------------
.. code-block:: bash

    nova aggregate-create Dell01 Dell01
    nova aggregate-create Dell02 Dell02
    nova aggregate-list

添加主机
---------------------
.. code-block:: bash

    nova aggregate-add-host Dell01 computer01.www.local
    nova aggregate-add-host Dell02 computer02.www.local

创建云主机类型
---------------------
.. code-block:: bash

    openstack flavor create --id 1 --vcpus 1 --ram 512 --disk 5  m1.nano

安全规则
---------------------
.. code-block:: bash

    openstack security group rule create --proto icmp default
    openstack security group rule create --proto tcp --dst-port 22 'default'

###------------------------

创建虚拟网络
---------------------
.. code-block:: bash

    openstack network create --share --external \
    --provider-physical-network provider \
    --provider-network-type flat net_10.2

创建子网
---------------------
.. code-block:: bash

    openstack subnet create --network net_10.2 \
    --allocation-pool start=10.2.1.200,end=10.2.1.220 \
    --dns-nameserver 172.16.11.14 --gateway 10.2.1.1 --subnet-range 10.2.1.0/24 \
    sub_net_10.2

    # ip netns
    # systemctl restart network
    # #单ip创建网络后，可能造成中断,需等待片刻，或重启系统


m1.nano 主机类型，net-id后面是网络ID号,Dell01 可用域
```````````````````````````````````````````````````````
.. code-block:: bash

    #创建虚拟机 kvm01-cirros

    NET=`openstack network list|grep 'net_10.2'|awk '{print $2}'`
    echo $NET
    nova boot --flavor m1.nano --image cirros \
    --nic net-id=$NET \
    --security-group default --key-name mykey \
    --availability-zone Dell01 \
    kvm01-cirros


