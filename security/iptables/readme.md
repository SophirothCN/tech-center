<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>


## Resource
url: http://blog.51cto.com/alsww/826926


### iptables 优先级顺序


iptables 多条规则有冲突的时候，排在上面的规则优先。

比如我们已经设置了 iptables -A INPUT -p udp --dport 53 -j REJECT

那么如果再执行iptables -A INPUT -p udp --dport 53 -s 180.169.223.10 -j ACCEPT ，则不会生效

-A参数是append，添加的规则会放在追后面，而前面已经有REJECT 该端口所有的访问了，那么这条ACCEPT就不会生效。

所以这里-A要改成-I，也就是insert的意思，插入一条记录，那么这条就会放在最前面，就在那条REJECT前面了，这样就能生效。





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

添加新的纪录,使用--reject-with icmp-net-unreachable

```bash
# iptables -A INPUT -p icmp -s 0.0.0.0/0 -j REJECT  --reject-with icmp-net-unreachable

```

那接下来，我们在访问该服务器的时候就是Unreachable了。

```
[root@dc ~]# ping dhcp.alv.pub -c 2
PING dhcp.alv.pub (192.168.127.1) 56(84) bytes of data.
From 192.168.127.1 (192.168.127.1) icmp_seq=1 Destination Net Unreachable
From 192.168.127.1 (192.168.127.1) icmp_seq=2 Destination Net Unreachable
```

- [x] drop


或者其实我们还可以直接掉掉包，不做响应。

还是先删除之前的规则
```
# iptables -D INPUT 1
# iptables -A INPUT -p icmp -s 0.0.0.0/0 -j drop

```

那么这个时候客户端来ping这个服务器的时候就不会收到之前那种不可达之类的提示了。下面我们是加了-c 2,表示只ping两次，如果没加那个，会一直那样等很久,得不到相应，这样的方式在防攻击的时候能起到一定的作用。

```bash
[root@dc ~]# ping dhcp.alv.pub -c 2
PING dhcp.alv.pub (192.168.127.1) 56(84) bytes of data.

--- dhcp.alv.pub ping statistics ---
2 packets transmitted, 0 received, 100% packet loss, time 1000ms

```