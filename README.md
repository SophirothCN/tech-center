
<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan'></a></p>

<p stype=font-weight:bold; align=center > <b>Alvin's Technology Center</b></p>

---

alv.pub（iP:47.75.0.56） 服务器提供以下服务：

- [x] 1 ntp服务。（时间同步服务。）
```bash
ntpdate alv.pub
```
- [x] 2 dns服务。（域名解析服务）
```bash
echo "nameserver 47.75.0.56" >> /etc/resolv.conf
```
- [x] 3 vpn服务。（个人使用，不对外开放）

- [x] 4 ldap服务。
```bash
yum install nss-pam-ldapd setuptool -y
authconfig --enableldap  --enableldapauth --ldapserver=ldap://natasha.alv.pub --disableldaptls  --enablemkhomedir --ldapbasedn="dc=alv,dc=pub" --update
mkdir -p /sophiroth/alvin
cp -p /etc/skel/.bash* /sophiroth/alvin
chown alvin:sophiroth /sophiroth/alvin -R
id alvin
su - alvin #密码是sophiroth,默认情况该账号拥有sudo权限
```
