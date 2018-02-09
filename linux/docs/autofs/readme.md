### 本文档讲述autofs的配置


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



