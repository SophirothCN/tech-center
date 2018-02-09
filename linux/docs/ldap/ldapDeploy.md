
 <html>
  <p align=center style="font-weight:bold;font-size=60px;"><b>部署ldap服务</b></p>
 
</html>


---
###  1. Server端安装
---

Step 1: Install the following packages:

---

```bash
yum install -y openldap openldap-clients openldap-servers migrationtools
```

Step 2: Configure OpenLDAP Server: 

```bash
vim /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{2\}hdb.ldif
change two lines:   #change  dc=yooma
olcSuffix: dc=yooma,dc=com               
olcRootDN: cn=root,dc=yooma,dc=com
add one line:
olcRootPW:	123456 #密码根据自己需要修改,主要密码前面是个tab
```

Step 3: Configure Monitoring Database Configuration file: 
```bash
 vim /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{1\}monitor.ldif
 #修改dn.base=""中的cn、dc项与step2中的相同
olcAccess: {0}to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=extern
al,cn=auth" read by dn.base="cn=root,dc=yooma,dc=com" read by * none
 ```

Step 4: Prepare the LDAP database:
```bash
cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
chown -R ldap.ldap /var/lib/ldap
```

Step 5: Test the configuration:
```bash
slaptest -u
56e7c83d ldif_read_file: checksum error on "/etc/openldap/slapd.d/cn=config/olcDatabase={1}monitor.ldif"
56e7c83d ldif_read_file: checksum error on "/etc/openldap/slapd.d/cn=config/olcDatabase={2}hdb.ldif"
config file testing succeeded  #验证成功
```


