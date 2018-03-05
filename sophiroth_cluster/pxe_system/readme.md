
#pxe + Kickstart 无人值守安装系统


- 安装软件
yum -y install tftp-server dhcp syslinux xinetd system-config-kickstart
cp /usr/share/doc/dhcp-4.2.5/dhcpd.conf.example /etc/dhcp/dhcpd.conf



参考：https://www.linuxidc.com/Linux/2017-06/144789.htm


系统内存要在2G以上，否则安装系统时容易报错。
