mysql error
#####################

.. contents::



Too many connections
``````````````````````````````
修改/etc/my.cnf这个文件，在[mysqld] 中新增max_connections=N，如果你没有这个文件请从编译源码中的support-files文件夹中复制你所需要的*.cnf文件为到 /etc/my.cnf。



设置为10000也可以。
max_connections=10000



Table 'mysql.column_stats' doesn't exist
````````````````````````````````````````````````

url:http://www.cnblogs.com/hankyoon/p/5197449.html


.. code-block:: sql

    解决方法：
    在主库创建以上表：
    CREATE TABLE IF NOT EXISTS `column_stats` (
    `db_name` varchar(64) NOT NULL COMMENT 'Database the table is in.',
    `table_name` varchar(64) NOT NULL COMMENT 'Table name.',
    `column_name` varchar(64) NOT NULL COMMENT 'Name of the column.',
    `min_value` varchar(255) DEFAULT NULL COMMENT 'Minimum value in the table (in text form).',
    `max_value` varchar(255) NOT NULL COMMENT 'Maximum value in the table (in text form).',
    `nulls_ratio` decimal(12,4) DEFAULT NULL COMMENT 'Fraction of NULL values (0 - no NULLs, 0.5 - half values are NULLs, 1 - all values are NULLs).',
    `avg_length` decimal(12,4) DEFAULT NULL COMMENT 'Average length of column value, in bytes. Counted as if one ran SELECT AVG(LENGTH(col)). This doesn''t count NULL bytes, assumes endspace removal for CHAR(n), etc.',
    `avg_frequency` decimal(12,4) DEFAULT NULL COMMENT 'Average number of records with the same value',
    `hist_size` tinyint(3) unsigned DEFAULT NULL COMMENT 'Histogram size in bytes, from 0-255.',
    `hist_type` enum('SINGLE_PREC_HB','DOUBLE_PREC_HB') DEFAULT NULL COMMENT 'Histogram type. See the histogram_type system variable.',
    `histogram` varbinary(255) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

    CREATE TABLE IF NOT EXISTS `index_stats` (
    `db_name` varchar(64) NOT NULL COMMENT 'Database the table is in.',
    `table_name` varchar(64) NOT NULL COMMENT 'Table name',
    `index_name` varchar(64) NOT NULL COMMENT 'Name of the index',
    `prefix_arity` int(10) unsigned NOT NULL COMMENT 'Index prefix length. 1 for the first keypart, 2 for the first two, and so on. InnoDB''s extended keys are supported.',
    `avg_frequency` decimal(12,4) DEFAULT NULL COMMENT 'Average number of records one will find for given values of (keypart1, keypart2, ..), provided the values will be found in the table.'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

    CREATE TABLE IF NOT EXISTS `table_stats` (
    `db_name` varchar(64) NOT NULL COMMENT 'Database the table is in .',
    `table_name` varchar(64) NOT NULL COMMENT 'Table name.',
    `cardinality` bigint(21) DEFAULT NULL COMMENT 'Number of records in the table.'
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

    ALTER TABLE `column_stats`
    ADD PRIMARY KEY (`db_name`,`table_name`,`column_name`);

    ALTER TABLE `index_stats`
    ADD PRIMARY KEY (`db_name`,`table_name`,`index_name`,`prefix_arity`);

    ALTER TABLE `table_stats`
    ADD PRIMARY KEY (`db_name`,`table_name`);