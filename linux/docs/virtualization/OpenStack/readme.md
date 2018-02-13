
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
yum install epel-release -y

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
