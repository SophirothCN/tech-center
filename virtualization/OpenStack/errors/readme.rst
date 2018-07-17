openstack error
#####################

.. contents::

QEMU version 2.1.0 or greater
`````````````````````````````````````
 yum remove qemu-system-x86


Could not access KVM kernel module: Permission denied
`````````````````````````````````````````````````````````````

failed to initialize KVM: Permission denied
No accelerator found!

是权限问题，做如下处理：

#chown root:kvm /dev/kvm

修改/etc/libvirt/qemu.conf，

#user="root"

user="root"

#group="root"

group="root"

重启服务

#service libvirtd restart，问题解决了