<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan'></a></p>




## 安装iotop

```
# yum install iotop -y
```

代码如下:
```txt
--version #显示版本号
-h, --help #显示帮助信息
-o, --only #显示进程或者线程实际上正在做的I/O，而不是全部的，可以随时切换按o
-b, --batch #运行在非交互式的模式
-n NUM, --iter=NUM #在非交互式模式下，设置显示的次数，
-d SEC, --delay=SEC #设置显示的间隔秒数，支持非整数值
-p PID, --pid=PID #只显示指定PID的信息
-u USER, --user=USER #显示指定的用户的进程的信息
-P, --processes #只显示进程，一般为显示所有的线程
-a, --accumulated #显示从iotop启动后每个线程完成了的IO总数
-k, --kilobytes #以千字节显示
-t, --time #在每一行前添加一个当前的时间
-q, --quiet #suppress some lines of header (implies --batch). This option can be specified up to three times to remove header lines.
-q column names are only printed on the first iteration,
-qq column names are never printed,
-qqq the I/O summary is never printed.
```
可用的命令（在运行iotop命令后按相应键位）：

使用left和right改变排序（方向键改变排序列），还可使用以下命令：


复制代码

代码如下:

r：反向排序，
o：切换至选项--only，
p：切换至--processes选项，
a：切换至--accumulated选项
q：退出
i：改变线程的优先级

例子：

```bash
# iotop
# iotop -b -n 3 -d 5
```

只显示有磁盘io的进程,以千字节显示

```bash
# iotop -P -k -o
```

只显示有磁盘io的进程,以千字节显示,非交互式显示，显示三次
```bash
# iotop -P -k -o -b -n3
```