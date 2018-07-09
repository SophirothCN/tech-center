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

echo "*      soft    nofile     65536" >> /etc/security/limits.conf
echo "*      hard    nofile     65536" >> /etc/security/limits.conf




查看当前系统下有哪些程序在运行（Running状态）
```````````````````````````````````

ps aux|egrep -v "aux|grep"|grep R
