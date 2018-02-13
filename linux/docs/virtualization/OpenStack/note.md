yum install ftp://ftp.ntua.gr/pub/linux/centos/7.4.1708/virt/x86_64/kvm-common/qemu-kvm-ev-2.9.0-16.el7_4.13.1.x86_64.rpm http://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/seavgabios-bin-1.10.2-3.el7_4.1.noarch.rpm http://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/seabios-bin-1.10.2-3.el7_4.1.noarch.rpm http://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/ipxe-roms-qemu-20170123-1.git4e85b27.el7_4.1.noarch.rpm -y


</br>

httpd 服务启动之后，如果那两个端口的内容无法正常访问，执行这个：keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone

</br>
参考文档：https://docs.openstack.org/mitaka/zh_CN/install-guide-rdo/keystone-install.html
