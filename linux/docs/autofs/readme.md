### 本文档讲述autofs的配置

#### 环境背景
---
目标ops1是一台ldap服务器，同时也是ldap用户的home目录数据存放的的服务器，那些目录在ops1上做了nfs共享，让客户端去挂载使用。</br>
我们在ldap客户端配置autofs自动挂载，当用户登陆ldap账号的时候，会自动进入到自己的home目录，在"进入用户自己的home目录"这个动作触发的时候，就触发了autofs的自动挂载，将用户的home目录给挂载过来。  用autofs做自动挂载，让我们在需要用到指定目录的时候才去挂载，不需要用到的时候就不挂载，合理的进行自动挂载。

<html>
<table>
    <thead>
        <th>Role</th>
        <th>Hostname</th>
        <th>OS</th>
        <th>User</th>
        <th>Selinux</th>
        <th>Firewalld</th>
    </thead>
    <tr>
        <td>Server</td>
        <td>ops1.alv.pub</td>
        <td>centos7.4</td>
        <td>root</td>
        <td>disabled</td>
        <td>disabled</td>
    </tr>
    <tr>
        <td>client</td>
        <td>ops2.alv.pub</td>
        <td>centos7.4</td>
         <td>root</td>
        <td>disabled</td>
        <td>disabled</td>
    </tr>
</table>
 </html>

#### 1 目标nfs服务的配置环境

 ```bash
 [root@ops1 ~]# cat /etc/exports
/ldapUserData/alvin *(rw,async)

[root@ops2 ~]# showmount -e ops1.alv.pub
Export list for ops1.alv.pub:
/ldapUserData *

```

#### 2 安装autofs
```bash
yum -y install autofs 
```
#### 3 配置autofs
```bash
echo "/sophiroth auto.sophiroth rw,nosuid --timeout=60" >>/etc/auto.master 
echo "* ops1.alv.pub:/ldapUserData/&" >> /etc/auto.sophiroth
```

#### 4 启动autofs，并设置开机自动启动
```bash
systemctl start autofs
systemctl enable autofs
```

#### 5 访问相关目录
```bash
[root@ops2 ~]# ll /sophiroth/alvin
ls: cannot open directory /sophiroth/alvin: Permission denied
[root@ops2 ~]# su - alvin
Last login: Fri Feb  9 05:20:54 EST 2018 on pts/2
[alvin@ops2 ~]$ pwd
/sophiroth/alvin
```
<img src=https://github.com/AlvinWanCN/TechnologyCenter/raw/master/linux/docs/autofs/img/autofs.jpg>

