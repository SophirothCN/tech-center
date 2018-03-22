<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>


## show


显示当前的mysql线程，如果有 SUPER 权限，则可以看到全部的线程，否则，只能看到自己发起的线程（这是指，当前对应的 MySQL 帐户运行的线程）。


```sql
show processlist;
```

show processlist命令可以看到有那些线程，还有一部分sql，但只会显示一部分sql，不会显示全部，有时候我们需要查看全部的sql吗，那怎么办呢？答案是，加个full就好了。

```sql
show full processlist;
```

那当有些线程持续了很久了，一条查询sql由于各种原因一直查了很久还在继续，也占用着高CPU,我们想要结束那条查询，怎么办呢？

那么我们可以kill掉它,通过前面的show命令我们可以看到所有线程的id，比如我们要结束的线程的id时候33，那么我们kill 33 就可以了。

```
kill 33
```