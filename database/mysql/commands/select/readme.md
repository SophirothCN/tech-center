<p align='center'> <a href='https://github.com/alvinwancn' target="_blank"> <img src='https://github.com/AlvinWanCN/life-record/raw/master/images/etlucency.png' alt='Alvin Wan' width=200></a></p>




##### 查询指定表指定字段后拼接指定字符。

example:

```sql
SELECT concat('DROP TABLE IF EXISTS ', table_name, ';')
FROM information_schema.tables
WHERE table_schema = 'mydb';
```
```sql
select CONCAT('My name is ',nickName,', I am happy.') from user where mobile = 13564107541
```

这里table_name, 和nickName，都是后面指定的表的字段。