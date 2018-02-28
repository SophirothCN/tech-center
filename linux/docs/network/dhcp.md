### 部署环境
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
        <td>dhcp.alv.pub</td>
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

---

---
###  1. Server端安装
---

#### Step 1: Install the following packages:

---

```bash
yum install -y dhcp
```


---
###  2. Server端配置
---

#### Step 2: Configure dhcp Server: 

-  配置DHCP服务
```
vim /etc/dhcp/dhcpd.conf
#设置DHCP于DNS服务器的动态信息更新模式。初学时完全可以不理这个选项，但是全局设置中一定要有这个选项，否则DHCP服务不能成功启动。
ddns-update-style interim;
subnet 192.168.38.0 netmask 255.255.255.0 {
    range 192.168.38.200 192.168.38.254; #分配给客户机的IP从192.168.233.100开始到192.168.233.199
    option routers 192.168.38.1; #设置网关
    default-lease-time 600; #默认租约时间
    max-lease-time 7200; #最大租约时间
}

```
- 为指定服务器网卡进行MAC地址与IP地址绑定，则继续在上面的配置文件下面进行如下配置
```
host ops2 { #有一个主机，叫ops2
    hardware ethernet 00:0c:29:1c:53:48; #MAC地址是08:...:27的网卡
    fixed-address 192.168.38.235;    #分配给它192.168.38.235的IP
}
```
