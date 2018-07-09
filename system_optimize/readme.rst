linux optimize
#########################

.. contents::

关机提示： a stop job is running for....
``````````````````````````````````````````````

 关机提示： a stop job is running for... 太耗时，

一、现象
-----------------

Linux关机或重启时提示A stop job is running for ..


导致关机慢。


二、解决方法
-------------------

编辑/etc/systemd/system.conf


修改下面两个变量为：


DefaultTimeoutStartSec=10s
DefaultTimeoutStopSec=10s
执行：systemctl daemon-reload
文章标签： kali linux linux


清理内存缓存
```````````````````

释放缓存区内存的方法
    a）清理pagecache（页面缓存）

1
# echo 1 > /proc/sys/vm/drop_caches     或者 # sysctl -w vm.drop_caches=1
　 b）清理dentries（目录缓存）和inodes

1
# echo 2 > /proc/sys/vm/drop_caches     或者 # sysctl -w vm.drop_caches=2
　 c）清理pagecache、dentries和inodes

1
# echo 3 > /proc/sys/vm/drop_caches     或者 # sysctl -w vm.drop_caches=3
　 上面三种方式都是临时释放缓存的方法，要想永久释放缓存，需要在/etc/sysctl.conf文件中配置：vm.drop_caches=1/2/3，然后sysctl -p生效即可！

    另外，可以使用sync命令来清理文件系统缓存，还会清理僵尸(zombie)对象和它们占用的内存

1
# sync


已打开文件达到上限(ulimit)
```````````````````````````

ulimit

设置系统打开文件数设置，解决高并发下 too many open files 问题。此选项直接影响单个进程容纳的客户端连接数。 Soft open files 是Linux系统参数，影响系统单个进程能够打开最大的文件句柄数量，这个值会影响到长连接应用如聊天中单个进程能够维持的用户连接数， 运行ulimit -n能看到这个参数值，如果是1024，就是代表单个进程只能同时最多只能维持1024甚至更少（因为有其它文件的句柄被打开）。如果开启4个进程维持用户连接，那么整个应用能够同时维持的连接数不会超过4*1024个，也就是说最多只能支持4x1024个用户在线可以增大这个设置以便服务能够维持更多的TCP连接。 Soft open files 修改方法：

ulimit -HSn 102400

这只是在当前终端有效，退出之后，open files 又变为默认值。

将ulimit -HSn 102400写到/etc/profile中

这样每次登录终端时，都会自动执行/etc/profile。

令修改open files的数值永久生效。

修改配置文件：/etc/security/limits.conf. 在这个文件后加上：

soft nofile 1024000
hard nofile 1024000
root soft nofile 1024000
root hard nofile 1024000

注意，修改limits.conf文件后，需要重启系统生效

也可用如下方式配置

echo "*      soft    nofile     65536" >> /etc/security/limits.conf
echo "*      hard    nofile     65536" >> /etc/security/limits.conf




查看当前系统下有哪些程序在运行（Running状态）
```````````````````````````````````

ps aux|egrep -v "aux|grep"|grep R

