
## Nginx的alias的用法及与root的区别
http://nginx.org/en/docs/http/ngx_http_core_module.html#alias

http://nginx.org/en/docs/http/ngx_http_core_module.html#root

以前只知道Nginx的location块中的root用法，用起来总是感觉满足不了自己的一些想法。然后终于发现了alias这个东西。

先看toot的用法

```
location /request_path/image/ {
    root /local_path/image/;
}
```

这样配置的结果就是当客户端请求 /request_path/image/cat.png 的时候，
Nginx把请求映射为/local_path/image/request_path/image/cat.png

再看alias的用法

```
location /request_path/image/ {
    alias /local_path/image/;
}
```

这时候，当客户端请求 /request_path/image/cat.png 的时候，
Nginx把请求映射为/local_path/image/cat.png
对比root就可以知道怎么用了吧~~ :)