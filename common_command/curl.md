<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>



## Resources

url: http://www.linuxdiyf.com/linux/2800.html

### curl 发送post请求，传参示例

```bash
curl -l -H Content-type:application/json -X POST --data '{"appVersion":"5.0.1","loginName":"17898852496","operatorUserId":"string","pageNo":"-1","password":"f379eaf3c831b04de153469d1bec345e","phoneType":"iPhone 7__iOS10.3.1","platformCode":"pangProApp","rowsPerPage":10,"sessionid":"8xxxx"}' http://cbp.shxxxh.com:556/shenmin-authority/authority/loginWithPassword
```

### curl下载东西。

```bash
curl -sSL http://www.golangtc.com/static/go/1.6.2/go1.6.2.linux-amd64.tar.gz -o o1.6.2.linux-amd64.tar.gz
```

### #查看目标服务器使用的web服务名称和版本

```bash
curl -I alv.pub
```

### 使用用户名和密码

```bash
curl -u alvin:wankaihao k8s.shenmin.com 
```


### 通过curl访问网站查看自己的公网IP

```
curl http://ipinfo.io/ip
```





### 执行网络脚本

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/AlvinWanCN/scripts/master/shell/sshslowly.sh)"
```
