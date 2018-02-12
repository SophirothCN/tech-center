<p align='center' >
  <a href='https://github.com/alvinwancn' target="_blank"> 
      <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=250>
  </a>
</p>
<p align=center ><b>Common Network Yum Repository</b></p>



[常见的一些网络yum源地址](#常见的一些网络yum源地址) </br>
[默认网络yum源](#默认网络yum源) </br>
[手动配置使用网络yum源](#手动配置使用网络yum源) </br>
[默认网络yum源](#默认网络yum源) </br>
[使用epel yum源](#使用epel的yum源) </br>
#### 常见的一些网络yum源地址

```text
http://mirror.bit.edu.cn/centos/
http://mirrors.aliyun.com/centos/
http://mirrors.zju.edu.cn/centos/
http://mirror.lzu.edu.cn/centos/
http://mirrors.sohu.com/centos/
http://mirrors.tuna.tsinghua.edu.cn/centos/
http://mirrors.cn99.com/centos/
http://mirrors.cqu.edu.cn/CentOS/
http://mirrors.nju.edu.cn/centos/
http://mirrors.163.com/centos/
```
---
#### 默认网络yum源
---

安装好系统之后，我们都会有默认的yum源，执行yum repolist 可以查看当前我们系统所使用的yum源。
```bash
[root@openstack ~]# ll /etc/yum.repos.d/
total 28
-rw-r--r--. 1 root root 1664 Aug 30 11:53 CentOS-Base.repo
-rw-r--r--. 1 root root 1309 Aug 30 11:53 CentOS-CR.repo
-rw-r--r--. 1 root root  649 Aug 30 11:53 CentOS-Debuginfo.repo
-rw-r--r--. 1 root root  314 Aug 30 11:53 CentOS-fasttrack.repo
-rw-r--r--. 1 root root  630 Aug 30 11:53 CentOS-Media.repo
-rw-r--r--. 1 root root 1331 Aug 30 11:53 CentOS-Sources.repo
-rw-r--r--. 1 root root 3830 Aug 30 11:53 CentOS-Vault.repo
```
这里我们查看一下其中一个文件CentOS-Base.repo的内容

```bash
[root@openstack ~]# grep -vE "^#|^$" /etc/yum.repos.d/CentOS-Base.repo 
[base]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
[updates]
name=CentOS-$releasever - Updates
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
[extras]
name=CentOS-$releasever - Extras
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
[centosplus]
name=CentOS-$releasever - Plus
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus&infra=$infra
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
```
我们会发现，配置文件的文件里有一行是mirrorlist,而我们平时自己配置本地yum仓库时，那里写的是baseurl，而不是mirrorlist，mirrorlsit的值是一个http链接，我们看到配置文件里这个链接中包含了一些变量，会根据不同的系统，而变为相应的内容。Alvin使用的系统是centos7.4.研究测试后发现，比如http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
 这个链接，最终这里面的变量取到值后，真实访问的完整链接是：http://mirror.bit.edu.cn/centos/7.4.1708/extras/x86_64/ ，而这个地址里的内容，则如下所示：
```text
http://mirror.bit.edu.cn/centos/7.4.1708/extras/x86_64/
http://mirrors.aliyun.com/centos/7.4.1708/extras/x86_64/
http://mirrors.zju.edu.cn/centos/7.4.1708/extras/x86_64/
http://mirror.lzu.edu.cn/centos/7.4.1708/extras/x86_64/
http://mirrors.sohu.com/centos/7.4.1708/extras/x86_64/
http://mirrors.tuna.tsinghua.edu.cn/centos/7.4.1708/extras/x86_64/
http://mirrors.cn99.com/centos/7.4.1708/extras/x86_64/
http://mirrors.cqu.edu.cn/CentOS/7.4.1708/extras/x86_64/
http://mirrors.nju.edu.cn/centos/7.4.1708/extras/x86_64/
http://mirrors.163.com/centos/7.4.1708/extras/x86_64/
```
以此判断，改yum仓库的配置，mirrorlist的配置，实际上是去找上门这个地址列表里的内容。

---
#### 手动配置使用网络yum源
---

比如我们要使用centos7的基础包，这里我们使用阿里云的网络yum源。 在配置里面，[centos7base]里中括号里的内容，是repo id,而下面的name，则是repo name，也就是仓库的名字，就像我们创建账号时一个是用户名一个是显示名。用户名是用来识别身份的，显示名则更多的用来展示、用来看的。
```bash
cat >/etc/yum.repos.d/centos7-base.repo<<EOF
[centos7base]
name=centos7-base
baseurl=http://mirrors.aliyun.com/centos/7/os/x86_64/
gpgcheck=0
enabled=1
EOF
```
或者我们要用docker，而基础包里没有docker，所以这里我们使用centos7的extras仓库，这个仓库里有docker-latest包，这里我们还是使用阿里云的，那么我们执行如下命令就好了：
```bash
cat >/etc/yum.repos.d/centos7-extras.repo<<EOF
[centos7extras]
name=centos7-extras
baseurl=http://mirrors.aliyun.com/centos/7/extras/x86_64/
gpgcheck=0
enabled=1
EOF
```
平时为了加快访问速度，如果常有新机安装，需要通过yum来安装软件，我们可以搭建一个本地的yum源服务器，然后把上面的baseurl后面的内容换成我们内网自己的服务器地址，那接下来我们安装软件时下载软件的速度就很快了。</br>
如果是本地挂载了光盘，比如将iso文件挂载到了/mnt/iso目录下，那么我们如果要使用本地的镜像里的软件作为yum源，则可以如下配置
```bash
cat >/etc/yum.repos.d/base.repo<<EOF
[base]
name=base
baseurl=file:///mnt/iso
gpgcheck=0
enabled=1
EOF
```
然后就可以使用了。

---
#### 使用epel的yum源
---
我们可以通过安装epel-release 这个rpm包来让我们拥有epel yum源。这个包在base仓库里面不存在，它存在于extras仓库里面。
```bash
yum install epel-release -y
```
完成安装后，我们可以在/etc/yum.repos.d/目录看到多了两个文件epel.repo和epel-testing.repo,然后执行yum repolist 可以看到epel仓库已加载可用了。这里我们只要用到的是/etc/yum.repos.d/epel.repo这个文件，我们来看一看这里面的内容,这里主要为我们提供包的，也是epel这个仓库。
```bash
[root@openstack ~]# cat /etc/yum.repos.d/epel.repo 
[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch
#baseurl=http://download.fedoraproject.org/pub/epel/7/$basearch
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch
failovermethod=priority
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

[epel-debuginfo]
name=Extra Packages for Enterprise Linux 7 - $basearch - Debug
#baseurl=http://download.fedoraproject.org/pub/epel/7/$basearch/debug
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-debug-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1

[epel-source]
name=Extra Packages for Enterprise Linux 7 - $basearch - Source
#baseurl=http://download.fedoraproject.org/pub/epel/7/SRPMS
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-source-7&arch=$basearch
failovermethod=priority
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
gpgcheck=1
```
