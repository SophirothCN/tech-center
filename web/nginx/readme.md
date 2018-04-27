<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>

[nginx显示文件夹目录](!让nginx显示文件夹目录)
[nginx匹配规则](!nginx匹配规则)
[nginx负载均衡](!nginx负载均衡)
[htpasswd安全验证](!htpasswd安全验证)


#### 让nginx显示文件夹目录



```conf
location ^~ /download {
        root /data/www/file                     //指定实际目录绝对路径；
        autoindex on;                            //开启目录浏览功能；
        autoindex_exact_size off;            //关闭详细文件大小统计，让文件大小显示MB，GB单位，默认为b；
        autoindex_localtime on;              //开启以服务器本地时区显示文件修改日期！
}
```


#### nginx匹配规则

例子，有如下匹配规则：

```
location = / {
   #规则A
}
location = /login {
   #规则B
}
location ^~ /static/ {
   #规则C
}
location ~ \.(gif|jpg|png|js|css)$ {
   #规则D
}
location ~* \.png$ {
   #规则E
}
location / {
   #规则F
}

```

那么产生的效果如下：
```
访问根目录 /， 比如 http://localhost/ 将匹配规则 A
访问 http://localhost/login 将匹配规则 B，http://localhost/register 则匹配规则 F
访问 http://localhost/static/a.html 将匹配规则 C
访问 http://localhost/a.gif, http://localhost/b.jpg 将匹配规则 D 和规则 E，但是规则 D 顺序优先，规则 E 不起作用，而 http://localhost/static/c.png 则优先匹配到规则 C
访问 http://localhost/a.PNG 则匹配规则 E，而不会匹配规则 D，因为规则 E 不区分大小写。
```


#### htpasswd安全验证

ubuntu下如何没有htpasswd命令要先安装apt-get install apache2-utils
注意写相对路径。


1、参考以下内容，修改配置文件：
```
server {
listen 80;
        location ^~ /download{
        auth_basic "secret";
        auth_basic_user_file /etc/nginx/db/passwd.db;
            autoindex on;
            autoindex_exact_size off;
            autoindex_localtime on;
            alias /opt/excel/;
        }

}
上面的配置表示将elk.yjmyzz.com的请求，转发到服务器的5601端口，同时使用最基本的用户名、密码来认证。

2、配置登录用户名，密码
1 htpasswd -c /data/nginx/db/passwd.db user1

注意将那个秘钥文件写相对路径，否则可能会有报错，相对于那个配置文件所在的路径。

#### 最简单的反向代理

server {
    charset utf-8;
    listen       80;
    server_name  u1.shenmin.com;

    location / {
        proxy_pass http://u1.shenmin.com:5000;
    }

}



#### nginx负载均衡

这里我们用的nginx版本是1.12.2，通过下面的配置，可以实现对c3.alv.pub 和c4.alv.pub web服务的高可用负载均衡，这种配置下，我们访问c1，会被平均分配到c3和c4上，如果c3或c4中有服务停掉，那么则不会被分配到，可以任意down掉一台。
做负载均衡。

```
upstream web {
    server c3.alv.pub;
    server c4.alv.pub;
}

server {
    charset utf-8;
    listen       80;
    server_name  c1.alv.pub c1;

    location / {
        proxy_pass http://web;
    }

}

```