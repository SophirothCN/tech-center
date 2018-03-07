#!/usr/bin/python
#conding:utf-8
import os
url='https://github.com/AlvinWanCN/TechnologyCenter/raw/master/sophiroth_cluster/dhcp.alv.pub/dhcpd/conf.d/dhcpd.conf'
file='/etc/dhcp/dhcpd.conf'
os.system('curl -fsSL %s > %s'%(url,file))
os.system('systemctl restart dhcpd') #dhcpd can not reload ,so we restart this service.