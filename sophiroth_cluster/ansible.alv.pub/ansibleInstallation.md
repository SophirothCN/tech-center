<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>

### ansible installation
```bash
# cat >/etc/yum.repos.d/centos7-extras.repo<<EOF
[centos7extras]
name=centos7-extras
baseurl=http://mirrors.aliyun.com/centos/7/extras/x86_64/
gpgcheck=0
enabled=1
EOF
# yum install ansible -y
```

### ansible configuraion

- step 1, make ssh key

```bash
# ssh-keygen #enter enter enter

```

- step 2, push ssh public key to destination host </br>
example host is dhcp.alv.pub </br>
```bash
# ssh-copy-id -i ~/.ssh/id_rsa.pub dhcp.alv.pub
```