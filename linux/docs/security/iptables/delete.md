<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>



#### 查询当前iptables的规则number
这里我们使用了这样几条命令
iptables -L -n --line-numbers    ##所有链的规则number

iptables -L INPUT --line-numbers ## 查看INPUT的

iptables -L OUTPUT --line-numbers ## 查看OUTPUT的

iptables -L FORWARD --line-numbers ##查看FORWARD的


```bash
[root@natasha ~]# iptables -L -n --line-numbers
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     icmp --  0.0.0.0/0            0.0.0.0/0            reject-with icmp-port-unreachable

Chain FORWARD (policy ACCEPT)
num  target     prot opt source               destination
1    DOCKER-ISOLATION  all  --  0.0.0.0/0            0.0.0.0/0
2    DOCKER     all  --  0.0.0.0/0            0.0.0.0/0
3    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0            ctstate RELATED,ESTABLISHED
4    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0
5    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0

Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     tcp  --  0.0.0.0/0            125.39.240.113       tcp dpt:80 reject-with icmp-port-unreachable
2    REJECT     tcp  --  0.0.0.0/0            61.135.157.156       reject-with icmp-port-unreachable

Chain DOCKER (1 references)
num  target     prot opt source               destination
1    ACCEPT     udp  --  0.0.0.0/0            172.17.0.2           udp dpt:4500
2    ACCEPT     udp  --  0.0.0.0/0            172.17.0.2           udp dpt:500
3    ACCEPT     tcp  --  0.0.0.0/0            172.17.0.3           tcp dpt:443
4    ACCEPT     tcp  --  0.0.0.0/0            172.17.0.3           tcp dpt:80

Chain DOCKER-ISOLATION (1 references)
num  target     prot opt source               destination
1    RETURN     all  --  0.0.0.0/0            0.0.0.0/0

[root@natasha ~]# iptables -L INPUT --line-numbers
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     icmp --  anywhere             anywhere             reject-with icmp-port-unreachable
[root@natasha ~]# iptables -L OUTPUT --line-numbers
Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     tcp  --  anywhere             no-data              tcp dpt:http reject-with icmp-port-unreachable
2    REJECT     tcp  --  anywhere             61.135.157.156       reject-with icmp-port-unreachable
[root@natasha ~]# iptables -L FORWARD --line-numbers
Chain FORWARD (policy ACCEPT)
num  target     prot opt source               destination
1    DOCKER-ISOLATION  all  --  anywhere             anywhere
2    DOCKER     all  --  anywhere             anywhere
3    ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
4    ACCEPT     all  --  anywhere             anywhere
5    ACCEPT     all  --  anywhere             anywhere
```

#### 根据编号删除规则

默认不指定表的时候，就是找的filter表，那这个时候我们要删除filter表里OUTPUT链里第二条规则，则需要执行iptables -D OUTPUT 2，如下所示：


```bash
[root@natasha ~]# iptables -L OUTPUT -n -t filter --line-numbers
Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     tcp  --  0.0.0.0/0            125.39.240.113       tcp dpt:80 reject-with icmp-port-unreachable
2    REJECT     tcp  --  0.0.0.0/0            61.135.157.156       reject-with icmp-port-unreachable
[root@natasha ~]# iptables -D OUTPUT 2
[root@natasha ~]# iptables -L OUTPUT -n -t filter --line-numbers
Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination
1    REJECT     tcp  --  0.0.0.0/0            125.39.240.113       tcp dpt:80 reject-with icmp-port-unreachable
[root@natasha ~]#

```

成功删除完成。