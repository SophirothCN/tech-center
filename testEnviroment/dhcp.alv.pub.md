
<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>

- dhcp.alv.pub basic information
```
Hostname:dhcp.alv.pub
NIC1 Type: NAT
NIC1 IP:192.168.127.1
NIC2 Type: VMnet1
NIC2 IP:192.168.38.1
Default Gateway:192.168.127.2
```


- System Preinstallation
```bash
bash -c "$(curl -fsSL https://github.com/AlvinWanCN/scripts/raw/master/common_tools/disableSeAndFir.sh)" #自定义脚本的方式关闭防火墙
python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/common_tools/pullLocalYum.py)" #添加本地yum仓库
python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/common_tools/joinNatashaLDAP.py)" #加入到我的ldap
python -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/shell/pxe/set_hostname.py)" #根据ip修改主机名
```
- Configuretion Information

```sybase
# yum install dhcp -y
# vim /etc/dhcp/dhcpd.conf
#设置DHCP于DNS服务器的动态信息更新模式。初学时完全可以不理这个选项，但是全局设置中一定要有这个选项，否则DHCP服务不能成功启动。
ddns-update-style none;
subnet 192.168.38.0 netmask 255.255.255.0 {
    range 192.168.38.100 192.168.38.200; #分配给客户机的IP从192.168.38.100开始到192.168.38.200
    option domain-name-servers 47.75.0.56,114,114,114,114; #dns地址。
    option domain-name "alv.pub shenmin.com sophiroth.com"; #dns域 search domain
    #option routers 192.168.38.1; #设置网关
    filename "pxelinux.0"; #pxe装系统时找tftp服务要的文件。
    next-server 192.168.38.111; #tftp的服务器地址
    default-lease-time 600; #默认租约时间
    max-lease-time 7200; #最大租约时间
}

subnet 192.168.127.0 netmask 255.255.255.0 {
    range 192.168.127.100 192.168.127.200;
    option domain-name-servers 47.75.0.56,114.114.114.114;
    option domain-name "alv.pub shenmin.com sophiroth.com";
    filename "pxelinux.0";
    next-server 192.168.11.111;
    option routers 192.168.127.254;
    default-lease-time 600;
    max-lease-time 7200;
}
#设置ip与mac地址绑定

host t5.nat { #有一个主机，叫t5
    hardware ethernet 00:00:00:00:00:01;#MAC地址是00:00:00:00:00:01的网卡
    fixed-address 192.168.127.55;  #分配给它192.168.127.55的IP
}
host zabbix.nat {
    hardware ethernet 00:00:00:00:00:51;
    fixed-address 192.168.127.51;
}
host t7.nat {
    hardware ethernet 00:00:00:00:00:77;
    fixed-address 192.168.127.77;
}
host t8.nat {
    hardware ethernet 00:00:00:00:00:78;
    fixed-address 192.168.127.78;
}
# systemctl restart dhcpd
# systemctl enable dhcpd
```
