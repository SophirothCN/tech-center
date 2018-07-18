elasticserach
##################

.. contents::




查看es的各个index状态
````````````````````````

curl -X GET http://elk.alv.pub:9200/_cat/indices?v=|less


删除指定索引
````````````````

curl -XDELETE  'http://elk.alv.pub:9200/logstash-2018.06.25'
curl -XDELETE  "http://elk.alv.pub:9200/*2017.03*
