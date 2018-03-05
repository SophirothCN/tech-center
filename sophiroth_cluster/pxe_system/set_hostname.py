#!/usr/bin/python
#coding:utf-8
import socket,os,re
#前面是主机名，后面是ip的最后一位地址
def makeAlvHost(hostname,ip):
    return {'ip': ip, 'hostname': hostname+'.alv.pub'}
hostDict={} #Define dict for hosts
hostDict['zabbix']=makeAlvHost('zabbix','51') #Define host
hostDict['db1']=makeAlvHost('db1','52')
hostDict['db2']=makeAlvHost('db2','53')
hostDict['dc']=makeAlvHost('dc','54')
hostDict['ansible']=makeAlvHost('ansible','55')


ipstr=os.popen('ip a s ens32|grep global').read() #获取关于ip信息的字符串
lastIPNumber=re.findall(r'\w\s(.*)\/',ipstr)[0].split('.')[-1]  #截取ip最后一位
defaultName='os'+str(lastIPNumber)+'.alv.pub' #定义默认主机名
os.system('hostname %s' % defaultName) #设置默认主机名
os.system('echo %s > /etc/hostname' % defaultName) #设置默认主机名
for hostname in hostDict:
    if hostDict[hostname]['ip'] == str(lastIPNumber):
        print(hostDict[hostname]['hostname'])
        break
