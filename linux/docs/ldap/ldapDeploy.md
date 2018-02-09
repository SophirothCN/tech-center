
 <html>
  <p align=center style="font-weight:bold;font-size=60px;"><b>部署ldap服务</b></p>
 
</html>

### 部署环境
<html>
<table>
    <thead>
        <th>Role</th>
        <th>Hostname</th>
        <th>OS</th>
        <th>Selinux</th
        <th>Firewalld</th
    </thead>
    <tr>
        <td>Server</td>
        <td>ops1.alv.pub</td>
        <td>centos7.4</td>
        <td>disabled</td>
        <td>disabled</td>
    </tr>
    <tr>
        <td>client</td>
        <td>ops2.alv.pub</td>
        <td>centos7.4</td>
        <td>disabled</td>
        <td>disabled</td>
    </tr>
</table>
 </html>

---
###  1. Server端安装
---

#### Step 1: Install the following packages:

---

```bash
yum install -y openldap openldap-clients openldap-servers migrationtools
```

#### Step 2: Configure OpenLDAP Server: 

```bash
vim /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{2\}hdb.ldif
change two lines:   #change  dc=yooma
olcSuffix: dc=yooma,dc=com               
olcRootDN: cn=root,dc=yooma,dc=com
add one line:
olcRootPW:	123456 #密码根据自己需要修改,主要密码前面是个tab
```

#### Step 3: Configure Monitoring Database Configuration file: 
```bash
 vim /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{1\}monitor.ldif
 #修改dn.base=""中的cn、dc项与step2中的相同
olcAccess: {0}to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=extern
al,cn=auth" read by dn.base="cn=root,dc=yooma,dc=com" read by * none
 ```

#### Step 4: Prepare the LDAP database:
```bash
cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
chown -R ldap.ldap /var/lib/ldap
```

#### Step 5: Test the configuration:
```bash
slaptest -u
56e7c83d ldif_read_file: checksum error on "/etc/openldap/slapd.d/cn=config/olcDatabase={1}monitor.ldif"
56e7c83d ldif_read_file: checksum error on "/etc/openldap/slapd.d/cn=config/olcDatabase={2}hdb.ldif"
config file testing succeeded  #验证成功
```

#### Step 6: Start and enable the slapd service at boot: 
```bash
systemctl start slapd
systemctl enable slapd
```

#### Step 7: Check the LDAP activity:
```bash
netstat -lt | grep ldap
netstat -tunlp | egrep "389|636"
```

#### Step 8: To start the configuration of the LDAP server, add the follwing LDAP schemas:
```bash
cd /etc/openldap/schema/
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f cosine.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f nis.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f collective.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f corba.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f core.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f duaconf.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f dyngroup.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f inetorgperson.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f java.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f misc.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f openldap.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f pmi.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f ppolicy.ldif
```
#### Step 9: Now use Migration Tools to create LDAP DIT: 
```
cd /usr/share/migrationtools/
vim migrate_common.ph 
on the Line Number 61, change "ou=Groups"
$NAMINGCONTEXT{'group'} = "ou=Groups";
on the Line Number 71, change your domain name
$DEFAULT_MAIL_DOMAIN = "yooma.com";
on the line number 74, change your base name
$DEFAULT_BASE = "dc=yooma,dc=com";
on the line number 90, change schema value
$EXTENDED_SCHEMA = 1;
```
####  Step 10: Generate a base.ldif file for your Domain DIT: 
```bash
 ./migrate_base.pl /root/base.ldif
 ```
 Step 11: Load "base.ldif" into LDAP Database: 
 ```bash
 ldapadd -x -W -D "cn=ops1,dc=alv,dc=pub" -f /root/base.ldif
  ```
  
#### Step 12: Now Create some users and Groups and migrate it from local database to LDAP 
  ```bash
mkdir /home/guests
useradd -d /home/guests/ldapuser1 ldapuser1
useradd -d /home/guests/ldapuser2 ldapuser2
echo 'password' | passwd --stdin ldapuser1
echo 'password' | passwd --stdin ldapuser
```

#### Step 13: Now filter out these Users and Groups and it password from /etc/shadow to different file: 
```bash
getent passwd | tail -n 5 > /root/users
getent shadow | tail -n 5 > /root/shadow
getent group | tail -n 5 > /root/groups
```
#### Step 14: Now you need to create ldif file for these users using migrationtools: 
```
 cd /usr/share/migrationtools
 vim migrate_passwd.pl
 #search /etc/shadow and replace it into /root/shadow on Line Number 188.
```
./migrate_passwd.pl /root/users > users.ldif
./migrate_group.pl /root/groups > groups.ldif
#### Step 15: Upload these users and groups ldif file into LDAP Database: 
```bash
 ldapadd -x -W -D "cn=root,dc=yooma,dc=com" -f users.ldif
 ldapadd -x -W -D "cn=root,dc=yooma,dc=com" -f 
 ```
#### Step 16: Now search LDAP DIT for all records: 
```bash
ldapsearch -x -b "dc=alv,dc=pub" -H ldap://ops1.alv.pub
```
###  1. Server端安装
```
yum install -y nss-pam*
authconfig-tui   #chose the secend [ Use LDAP] and next
su ldapuser1
bash-4.2$     #测试成功
```
