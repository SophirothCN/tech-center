mysql error
#####################





Too many connections
``````````````````````````````
修改/etc/my.cnf这个文件，在[mysqld] 中新增max_connections=N，如果你没有这个文件请从编译源码中的support-files文件夹中复制你所需要的*.cnf文件为到 /etc/my.cnf。



设置为10000也可以。
max_connections=10000