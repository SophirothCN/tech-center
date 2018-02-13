
<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>
<p align=center><b><u>Alvin's OpenStack Installation Notes</u></b></p>

官方文档：官方文档 http://docs.openstack.org </br>

### 部署环境
<html>
<table>
    <thead>
        <th>Role</th>
        <th>Hostname</th>
        <th>IP</th>
        <th>OS</th>
        <th>User</th>
        <th>Selinux</th>
        <th>Firewalld</th>
    </thead>
    <tr>
        <td>Node1</td>
        <td>ops1.alv.pub</td>
        <td>192.168.38.101</td>
        <td>centos7.4</td>
        <td>root</td>
        <td>disabled</td>
        <td>disabled</td>
    </tr>
    <tr>
        <td>Node2</td>
        <td>ops2.alv.pub</td>
        <td>192.168.38.102</td>
        <td>centos7.4</td>
         <td>root</td>
        <td>disabled</td>
        <td>disabled</td>
    </tr>
</table>
 </html>


#### 安装OpenStack
```


ops1:
cat >/etc/yum.repos.d/centos7-extras.repo<<EOF
[centos7extras]
name=centos7-extras
baseurl=http://mirrors.aliyun.com/centos/7/extras/x86_64/
gpgcheck=0
enabled=1
EOF

yum repolist
#Base
yum install epel-release -y
yum install -y centos-release-openstack-pike
yum install -y python-openstackclient
##MySQL
yum install -y mariadb mariadb-server MySQL-python
##RabbitMQ
yum install -y rabbitmq-server
##Keystone
yum install -y openstack-keystone httpd mod_wsgi memcached python-memcached
##Glance
yum install -y openstack-glance python-glance python-glanceclient
##Nova
yum install -y openstack-nova-api openstack-nova-cert openstack-nova-conductor openstack-nova-console openstack-nova-novncproxy openstack-nova-scheduler python-novaclient
##Neutron linux-node1.example.com
yum install -y openstack-neutron openstack-neutron-ml2 openstack-neutron-linuxbridge python-neutronclient ebtables ipset
##Dashboard
yum install -y openstack-dashboard
##Cinder
yum install -y openstack-cinder python-cinderclient

ops2:
cat >/etc/yum.repos.d/centos7-extras.repo<<EOF
[centos7extras]
name=centos7-extras
baseurl=http://mirrors.aliyun.com/centos/7/extras/x86_64/
gpgcheck=0
enabled=1
EOF

yum repolist
yum install epel-release -y
yum install -y centos-release-openstack-pike
yum install python-openstackclient
##Nova linux-node2.openstack
yum install ftp://ftp.ntua.gr/pub/linux/centos/7.4.1708/virt/x86_64/kvm-common/qemu-kvm-ev-2.9.0-16.el7_4.13.1.x86_64.rpm http://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/seavgabios-bin-1.10.2-3.el7_4.1.noarch.rpm http://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/seabios-bin-1.10.2-3.el7_4.1.noarch.rpm http://rpmfind.net/linux/centos/7.4.1708/updates/x86_64/Packages/ipxe-roms-qemu-20170123-1.git4e85b27.el7_4.1.noarch.rpm -y
yum install -y openstack-nova-compute sysfsutils
##Neutron linux-node2.openstack
yum install -y openstack-neutron openstack-neutron-linuxbridge ebtables ipset
##Cinder
yum install -y openstack-cinder python-cinderclient targetcli python-oslo-policy

ops1:
yum install -y chrony
vim /etc/chrony.conf
allow 192.168.0.0/16
systemctl enable chronyd.service
systemctl start chronyd.service
timedatectl set-timezone Asia/Shanghai
timedatectl status

ops2:
yum install -y chrony
vim /etc/chrony.conf
server 192.168.38.101 iburst #只留一行
systemctl enable chronyd.service
systemctl start chronyd.service
timedatectl set-timezone Asia/Shanghai
chronyc sources

ops1:
cp /usr/share/mariadb/my-medium.cnf /etc/my.cnf
vim /etc/my.cnf
[mysqld]
default-storage-engine = innodb
innodb_file_per_table
collation-server = utf8_general_ci
init-connect = 'SET NAMES utf8'
character-set-server = utf8


systemctl enable mariadb.service
mysql_install_db --datadir="/var/lib/mysql" --user="mysql"
systemctl start mariadb.service
mysql_secure_installation   #设置密 码及初始化 密码 123456，一路 y 回车
mysql -p123456
CREATE DATABASE keystone;
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'k eystone';
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'keyston e';
CREATE DATABASE glance;
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' IDENTIFIED BY 'glance';
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' IDENTIFIED BY 'glance';
CREATE DATABASE nova;
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' IDENTIFIED BY 'nova';
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' IDENTIFIED BY 'nova';
CREATE DATABASE neutron;
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' IDENTIFIED BY 'neu tron';
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' IDENTIFIED BY 'neutron';
CREATE DATABASE cinder;
GRANT ALL PRIVILEGES ON cinder.* TO 'cinder'@'localhost' IDENTIFIED BY 'cinder';
GRANT ALL PRIVILEGES ON cinder.* TO 'cinder'@'%' IDENTIFIED BY 'cinder'; 
flush privileges; 
show databases;

systemctl enable rabbitmq-server.service
systemctl start rabbitmq-server.service
rabbitmqctl add_user openstack openstack
rabbitmqctl set_permissions openstack ".*" ".*" ".*" 
rabbitmq-plugins list
rabbitmq-plugins enable rabbitmq_management #启动插件
systemctl restart rabbitmq-server.service
