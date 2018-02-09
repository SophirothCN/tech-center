
 <html>
  <p align=center style="font-weight:bold;font-size=60px;"><b>部署ldap服务</b></p>
 
</html>


---
###  1. Server端安装
---

Step 1: Install the following packages:

---

```
yum install -y openldap openldap-clients openldap-servers migrationtools
```

Step 2: Configure OpenLDAP Server: 

```
vim /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{2\}hdb.ldif
change two lines:   #change  dc=yooma
olcSuffix: dc=yooma,dc=com               
olcRootDN: cn=root,dc=yooma,dc=com
add one line:
olcRootPW:	123456 #密码根据自己需要修改,主要密码前面是个tab
```

Step 3: Configure Monitoring Database Configuration file: 
```
 vim /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{1\}monitor.ldif
 #修改dn.base=""中的cn、dc项与step2中的相同
olcAccess: {0}to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=extern
al,cn=auth" read by dn.base="cn=root,dc=yooma,dc=com" read by * none
 ```
