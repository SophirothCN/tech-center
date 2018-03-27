<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>



## 本地端口转发为目标服务器器指定端口

## 将本地192.168.38.1端口上的80转发到192.168.127.51的80上。

```bash
iptables -t nat -I PREROUTING -d 192.168.38.1 -p tcp --dport 80 -j DNAT --to-destination 192.168.127.51:80
```
上面这条规则配置了如何过去转发本地80到目标服务器，但是数据回来之后还要伪装修改一下才能返回给客户端，需要还需要添加一条。
所有来自192.168.38.0网段的对于目标服务器192.168.127.51的tcp端口为80的请求，都伪装成本服务器
如果使用-s -d -p --dport -o 之类的参数，就是默认对所有都开放。不指定网段，不指定端口，那么所有通过该服务器装发出去的对所有端口的请求，都会变成该服务器发出的请求。

```
iptables -t nat -I POSTROUTING -s 192.168.38.0/24 -d 192.168.127.51 -p tcp --dport 80 -j MASQUERADE
```

或者可以用下面的命令，将-j MASQUERADE换成--to-source 192.168.127.1，效果是一样的，只是指定了ip。 这两条命令用其中一条就可以了，
```
iptables -t nat -I POSTROUTING -s 192.168.38.0/24 -d 192.168.127.51 -p tcp --dport 80 -j SNAT --to-source 192.168.127.1

```

## 本地端口转发到本地其他端口

将80端口转发到8080

```bash
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```