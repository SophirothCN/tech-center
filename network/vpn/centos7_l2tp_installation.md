# 1, Install software
```
yum install -y xl2tpd libreswan lsof
```
# 2, configure service
## 2.1, configure /etc/xl2tpd/xl2tpd.conf
```
vim /etc/xl2tpd/xl2tpd.conf
[lns default]
ip range = 192.168.110.128-192.168.110.254
local ip = 192.168.110.99
require chap = yes
refuse pap = yes
require authentication = yes
name = LinuxVPNserver
ppp debug = yes
pppoptfile = /etc/ppp/options.xl2tpd
length bit = yes

```

## 2.2, configure /etc/ppp/options.xl2tpd
```sybase
vim /etc/ppp/options.xl2tpd
ipcp-accept-local
ipcp-accept-remote
ms-dns  8.8.8.8
ms-dns 209.244.0.3
ms-dns 208.67.222.222
name xl2tpd
#noccp
auth
crtscts
idle 1800
mtu 1410         #第一次配置不建议设置mtu，mru，否则可能789错误
mru 1410
nodefaultroute
debug
lock
proxyarp
connect-delay 5000
refuse-pap
refuse-chap
refuse-mschap
require-mschap-v2
persist
logfile /var/log/xl2tpd.log

```
## 2.3, configure /etc/ipsec.d/l2tp-ipsec.conf 
```
vim /etc/ipsec.d/l2tp-ipsec.conf
conn L2TP-PSK-NAT
    rightsubnet=0.0.0.0/0
    dpddelay=10
    dpdtimeout=20
    dpdaction=clear
    forceencaps=yes
    also=L2TP-PSK-noNAT
conn L2TP-PSK-noNAT
    authby=secret
    pfs=no
    auto=add
    keyingtries=3
    rekey=no
    ikelifetime=8h
    keylife=1h
    type=transport
    left=192.168.0.17   #service/VPS的外网地址，某些vps只有eth0一块网卡的，
                        #就填内网地址，内核开启nat转发就可以了，
                        #CentOS7以下的用iptables定义转发规则
    leftprotoport=17/1701
    right=%any
    rightprotoport=17/%any
```

## 2.4, configure /etc/ppp/chap-secrets
```sybase
vim /etc/ppp/chap-secrets
vpnuser * pass * 
```

## 2.5 configure /etc/ipsec.secrets
```
vim  /etc/ipsec.secrets
: PSK "sophiroth"
```

# 3， startup service
systemctl enable ipsec
systemctl restart ipsec
systemctl enable xl2tpd
systemctl restart xl2tpd

如果设置了防火，在防火墙打开1701和4500端口，udp协议。 （该文档可能存在问题）