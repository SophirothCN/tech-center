yum repository directory
#################################



add centos7 base
``````````````````````````

.. code-block:: bsah

    curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/tech-center/master/software/yum.repos.d/centos7.dc.alv.pub.repo > /etc/yum.repos.d/centos7.dc.alv.pub.repo

add epel repository
````````````````````````

.. code-block:: bash

    curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/tech-center/master/software/yum.repos.d/epel.dc.alv.pub.repo > /etc/yum.repos.d/epel.dc.alv.pub.repo

dd zabbix 3.4 yum reposiroty
``````````````````````````````````

.. code-block:: bash

    curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/tech-center/master/software/yum.repos.d/zabbix3.4.repo > /etc/yum.repos.d/zabbix3.4.repo



add openstack pick centos7 yum reposiroty
```````````````````````````````````````````

.. code-block:: bash

    curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/tech-center/master/software/yum.repos.d/openstack_pick_centos7.repo > /etc/yum.repos.d/openstack_pick_centos7.repo


add openstack queens repository
```````````````````````````````````````

.. code-block:: bash

    curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/tech-center/master/software/yum.repos.d/queens.repo > /etc/yum.repos.d/queens.repo
