#!/usr/bin/python
#coding:utf-8
import os
url='https://github.com/AlvinWanCN/TechnologyCenter/raw/master/sophiroth_cluster/alv.pub/named/alv.pub.zone'
file='/etc/ansible/hosts'
#serviceName='ansible'
os.system('curl -fsSL %s > %s'%(url,file))
#os.system('systemctl reload %s'%serviceName)