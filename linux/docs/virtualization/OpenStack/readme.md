
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
#yum install -y centos-release-openstack-pike
yum install -y yum install ftp://ftp.icm.edu.pl/vol/rzm6/linux-centos-vault/7.1.1503/extras/x86_64/Packages/centos-release-openstack-liberty-1-4.el7.noarch.rpm
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
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'keystone';
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'keystone';
CREATE DATABASE glance;
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' IDENTIFIED BY 'glance';
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' IDENTIFIED BY 'glance';
CREATE DATABASE nova;
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' IDENTIFIED BY 'nova';
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' IDENTIFIED BY 'nova';
CREATE DATABASE neutron;
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' IDENTIFIED BY 'neutron';
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

openssl rand -hex 10 #取一个随机数
d84fe5db185bc6a3b464
vim /etc/keystone/keystone.conf
cat /etc/keystone/keystone.conf|grep -v "^#"|grep -v "^$"
[DEFAULT]
admin_token = d84fe5db185bc6a3b464                                    #设置 token，和上面产生的随机数值一致 verbose = true
[assignment]
[auth]
[cache]
[catalog]
[cors]
[cors.subdomain]
[credential]
[database]
connection = mysql://keystone:keystone@192.168.38.101/keystone                                          #设置数 据库连接 写到 database 下
[domain_config]
[endpoint_filter]
[endpoint_policy]
[eventlet_server]
[eventlet_server_ssl]
[federation]
[fernet_tokens]
[identity]
[identity_mapping]
[kvs]
[ldap]
[matchmaker_redis]
[matchmaker_ring]
[memcache]
servers = 192.168.38.101:11211
[oauth1]
[os_inherit]
[oslo_messaging_amqp]
[oslo_messaging_qpid]
[oslo_messaging_rabbit]
[oslo_middleware]
[oslo_policy]
[paste_deploy]
[policy]
[resource]
[revoke]
driver = sql
[role]
[saml]
[signing]
[ssl]
[token]
provider = uuid
driver = memcache
[tokenless_auth]
[trust]

su -s /bin/sh -c "keystone-manage db_sync" keystone
systemctl enable memcached
systemctl start memcached
vim /etc/httpd/conf/httpd.conf
ServerName 192.168.38.101:80
vim /etc/httpd/conf.d/wsgi-keystone.conf
cat /etc/httpd/conf.d/wsgi-keystone.conf
Listen 5000
Listen 35357
<VirtualHost *:5000>
WSGIDaemonProcess keystone-public processes=5 threads=1 user=keystone group=keystone display-name=%{GROUP}
WSGIProcessGroup keystone-public
WSGIScriptAlias / /usr/bin/keystone-wsgi-public
WSGIApplicationGroup %{GLOBAL}
WSGIPassAuthorization On
<IfVersion >= 2.4>
ErrorLogFormat "%{cu}t %M"
</IfVersion>
ErrorLog /var/log/httpd/keystone-error.log
CustomLog /var/log/httpd/keystone-access.log combined
<Directory /usr/bin>
<IfVersion >= 2.4>
Require all granted
</IfVersion>
<IfVersion < 2.4>
Order allow,deny
Allow from all
</IfVersion>
</Directory>
</VirtualHost>
<VirtualHost *:35357>
WSGIDaemonProcess keystone-admin processes=5 threads=1 user=keystone group=keystone display-name=%{GROUP}
WSGIProcessGroup keystone-admin
WSGIScriptAlias / /usr/bin/keystone-wsgi-admin
WSGIApplicationGroup %{GLOBAL}
WSGIPassAuthorization On
<IfVersion >= 2.4>
ErrorLogFormat "%{cu}t %M"
</IfVersion>
ErrorLog /var/log/httpd/keystone-error.log
CustomLog /var/log/httpd/keystone-access.log combined
<Directory /usr/bin>
<IfVersion >= 2.4>
Require all granted
</IfVersion>
<IfVersion < 2.4>
Order allow,deny
Allow from all
</IfVersion>
</Directory>
</VirtualHost>

systemctl enable httpd
systemctl start httpd
netstat -lntup|grep http
export OS_TOKEN=d84fe5db185bc6a3b464
export OS_URL=http://192.168.38.101:35357/v3
export OS_IDENTITY_API_VERSION=3
keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone
openstack domain create  default
openstack project create --domain default --description "Admin Project" admin
openstack user create --domain default --password-prompt admin
openstack role create admin
openstack role add --project admin --user admin admin
openstack project create --domain default --description "Demo Project" demo 
openstack user create --domain default --password=demo demo
openstack role create user
openstack role add --project demo --user demo user
openstack project create --domain default --description "Service Project" service
openstack user list
openstack project list
openstack service create --name keystone --description "OpenStack Identity" identity
openstack endpoint create --region RegionOne identity public http://192.168.38.101:5000/v2.0
openstack endpoint create --region RegionOne identity internal http://192.168.38.101:5000/v2.0
openstack endpoint create --region RegionOne identity admin http://192.168.38.101:35357/v2.0
openstack endpoint list #查看
openstack endpoint delete ID #使用这个命令删除
unset OS_TOKEN
unset OS_URL
openstack --os-auth-url http://192.168.38.101:35357/v3 \
--os-project-domain-id default --os-user-domain-id default \
--os-project-name admin --os-username admin --os-auth-type password token issue

```
