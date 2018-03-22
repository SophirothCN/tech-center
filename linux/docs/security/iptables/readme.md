<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>

### example iptables 
```bash


#!/bin/bash
iptables -F
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p icmp -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp -s 192.168.105.4 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p tcp --dport 2049 -j ACCEPT
iptables -A INPUT -s 192.168.105.0/24 -j ACCEPT
iptables -A INPUT -j REJECT
iptables -A INPUT -j REJECT --reject-with icmp-host-prohibited
iptables -A FORWARD -j REJECT --reject-with icmp-host-prohibited
service iptables save
```


## 禁止ping

ping命令使用的是icmp协议，所以如果要禁止别人来ping我们的服务器，我们可以做如下设置。

正常情况下可以ping通目标主机
```
[root@dhcp ~]# ping 192.168.127.51
PING 192.168.127.51 (192.168.127.51) 56(84) bytes of data.
64 bytes from 192.168.127.51: icmp_seq=1 ttl=64 time=0.232 ms
64 bytes from 192.168.127.51: icmp_seq=2 ttl=64 time=0.317 ms
```

- [x]  --reject-with icmp-host-prohibited

现在目标主机添加一条iptables规则，这里我们设置的是拒绝任何网段来ping 拒绝的方式是--reject-with icmp-host-prohibited
```bash
[root@zabbix ~]# sudo iptables -A INPUT -p icmp -s 0.0.0.0/0 -j REJECT  --reject-with icmp-host-prohibited
```

#### 效果
然后再ping的时候，就发现ping不同了，显示Destination Host Prohibited

```bash
[root@dhcp ~]# ping 192.168.127.51 -c 2
PING 192.168.127.51 (192.168.127.51) 56(84) bytes of data.
From 192.168.127.51 icmp_seq=1 Destination Host Prohibited
From 192.168.127.51 icmp_seq=2 Destination Host Prohibited

--- 192.168.127.51 ping statistics ---
2 packets transmitted, 0 received, +2 errors, 100% packet loss, time 999ms

```
- [x] --reject-with icmp-net-unreachable

那么现在我们再用另一种方式去禁止ping，那就是--reject-with icmp-net-unreachable

先删除之前的记录,查看规则的number后删除对应的规则
```
[root@zabbix ~]# iptables -L INPUT --line-numbers
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     icmp --  anywhere             anywhere             reject-with icmp-host-prohibited
[root@zabbix ~]# iptables -D INPUT 1
[root@zabbix ~]# iptables -L INPUT --line-numbers
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination
[root@zabbix ~]#
```