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
        <td>dns.alv.pub</td>
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
yum install -y bind
```


---
###  2. Server端配置
---

#### Step 2: Configure dns Server: 

-  配置dns服务
```
vim /etc/named.conf
options {
        listen-on port 53 { any; };
        directory       "/var/named";
        allow-query     { any; };
        allow-update    {192.168.0.0/16;};
};

zone "." IN {
        type hint;
        file "named.ca";
};

include "/etc/named.rfc1912.zones";

```

```bash
vim /etc/named.rfc1912.zones
zone "shenmin.com" IN {
        type master;
        file "shenmin.com.zone";
        allow-update { 192.168.1.0/24; };
};
zone "alv.pub" IN {
        type master;
        file "alv.pub.zone";
        allow-update { 192.168.0.0/16; };
};
zone "sophiroth.com" IN {
        type master;
        file "sophiroth.com.zone";
        allow-update { 192.168.0.0/16; };

};
~  

```
```
vim /var/named/alv.pub.zone
$TTL 1D
@       IN SOA  @ root.alv.pub.zone. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
        NS      alv.pub.
@       A       47.75.0.56
c1      A       192.168.38.3
c1      A       192.168.1.131
c2      A       192.168.1.132
c3      A       192.168.1.133
c4      A       192.168.1.134

```
```bash
vim /var/named/shenmin.com.zone
$TTL 1D
@       IN SOA  @ root.shenmin.com.zone. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
        NS      shenmin.com.
@       A   47.75.0.56
natasha A   47.75.0.56
tuleap     A       192.168.1.203
test1   A       192.168.1.211
test2   A       192.168.1.212
```
```bash
vim /var/named/sophiroth.com.zone
$TTL 1D
@       IN SOA  @ root.sophiroth.com.zone. (
                                        0       ; serial
                                        1D      ; refresh
                                        1H      ; retry
                                        1W      ; expire
                                        3H )    ; minimum
        NS      sophiroth.com.
@       A   47.75.0.56
natasha A   47.75.0.56
nds     A   192.168.38.3
```
- 修改文件权限
```bash
chown named:named /var/named/ -R

```
- 我们的服务器没有配置ipv6地址，所以这里我们也禁用ipv6
```bash
vim /etc/sysconfig/named 
OPTIONS="-4"
```
- 然后启动服务
```bash
systemctl start named

```

---
###  3. Client端验证
---
- 客户端指定dns服务器地址和域
```
vim /etc/resolv.conf
search alv.pub shenmin.com sophiroth.com
nameserver 192.168.38.3

```
- 在添加了以上配置后，可以使用dns服务了，这里我们特地安装一个dns客户端工具来查看更详细的信息。
```bash
yum install bind-utils -y
```
- 测试

```bash
nslookup test1
nslookup sophiroth.com
nslookup c1.alv.pub
```
