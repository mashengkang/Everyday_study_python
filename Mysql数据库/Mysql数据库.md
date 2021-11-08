#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Mysql数据库

- 什么是数据库

> 数据库(Database)就是按照数据结构来组织,存储和管理数据的仓库
>
> 专业的数据库是专门对数据进行创建,访问,管理,搜索等操作的软件,比起我们自己用文件读写的方式对数据进行管理更加的方便,快速,安全

- 作用

  - 对数据进行持久化的保存
  - 方便数据的存储和查询,速度快,安全,方便
  - 可以处理并发访问
  - 更加安全的权限管理访问机制

- 常见的数据库

  > 数据库分两大类: 一类是 关系型数据库,另一类叫做非关系型数据库

  - 关系型数据库:Mysql ,Oracle,PostgreSQL, SQLserver...
  - 非关系型数据库:Redis内存数据库,MongoDB文档数据库

- 认识mysql数据库

  > Mysql是最流行的关系型数据库管理系统

  - 安装mysql

  windows:

  1. 在Mysql官网:https://dev.mysql.com/downloads/mysql/上面下载ZIP安装包(**Windows (x86, 64-bit), ZIP Archive**)

  2. 将安装包放在某文件夹解压

  3. 新建一个my.ini配置文件,在和bin的同级目录下,my.ini的内容如下:

     > 其中的url根据自己的解压路径进行填写

     ```ini
     [mysqld]
     #设置3306端口
     port=3306
     #设置mysql的安装目录
     basedir=F:\Down Tools\mysql-8.0.20-winx64
     #设置mysql数据库的数据的存放目录
     datadir=F:\Down Tools\mysql-8.0.20-winx64\Data
     #允许最大连接数
     max_connections=200
     #允许连接失败的次数。
     max_connect_errors=10
     #服务端使用的字符集默认为utf8mb4
     character-set-server=utf8mb4
     #创建新表时将使用的默认存储引擎
     default-storage-engine=INNODB
     #默认使用“mysql_native_password”插件认证
     #mysql_native_password
     default_authentication_plugin=mysql_native_password
     [mysql]
     #设置mysql客户端默认字符集
     default-character-set=utf8mb4
     [client]
     #设置mysql客户端连接服务端时默认使用的端口
     port=3306
     default-character-set=utf8mb4
     ```

  4. 在bin同级目录新建Data空文件夹

  5. 学习具体的方法链接:https://www.runoob.com/mysql/mysql-install.html

- 关于数据库的一些概念
  - 数据库 Database
  - 数据表 table
  - 数据字段
  - 行 row
  - 列

## Mysql基础操作(基础认识)

> 使用方法:
>
> 方式一:通过图形界面工具,如Navicat等(在熟练掌握后再使用)
>
> 方式二:通过命令行敲命令来操作(有助于命令的掌握)
>
> 方式三:通过编程语言执行Mysql命令

### **1.SQL结构化查询语言**

> SQL语言分为4个部分:DDL(定义),DML(操作),DQL(查询),DCL(控制)

### **Sql语句中的快捷键**

> \G 格式化输出 (文本式,竖立显示)
>
> \s 查看服务器端信息
>
> \c 结束命令出入操作
>
> \q 退出当前sql命令行模式
>
> \h 查看帮助

### 2.操作数据库的步骤

> 连接-->打开库-->操作-->关闭退出

```mysql
mysql -h localhost -u root -p
```

`-h`服务器地址

`-u`登录账号

`-p`回车后输入密码

`-P`(大写)端口号

### 3.数据库语法的特点

1. sql语句可以换行,要以分号结尾
2. 命令不区分大小写,关键字和函数建议用大写
3. 如果提示符为'> 那么需要输入一个回车
4. 命令打错了换行后不能修改,可以用\c取消

### 4.数据库操作

查看数据库 

```mysql
# 查看所有库
show databases;
```

创建数据库 

```mysql
# 链接mysql数据库后,进入mysql后可以操作数据
# 创建库
create database if not exists users default charset=utf8;
-- 1.数据库 users 如果不存在则创建数据库,存在则不创建
-- 2.创建users数据库,并设置字符集为utf8
-- 3.无特殊情况都要求字符集为utf8或者utf8mb4的字符编码
```

删除数据库 drop database 库名;

```mysql
# 因为python-04中有符号'-',所以可以用反引号括起来库名
drop database `python-04`;
```

打开数据库 

```mysql
# use 库名
use users
```



### 5.数据表的操作

> 数据库管理系统中,可以有很多库,每个数据库中可以包括多张数据表

#### 创建表的基本原则

- 表名和字段名,尽可能的符合命名规范,并且最好见名知意
- 表中数据必须有唯一标识,即主键定义,无特殊情况,主键都为数字并自增即可
- 表中字段所对应的类型设置合理,并限制合理长度
- 表引擎推荐使用`innodb`,并无特殊情况都要求为`utf8`或者`utf8mb4`的字符编码

#### **查看表** 

```mysql
show tables;
```

#### **创建表**

```mysql
# 以下创建一个users的表
create table users(
	-- 创建ID字段,为正整数,不允许为空, 主键,自动递增
	id int unsigned not null primary key auto_increment,
	-- 创建 存储 名字的字段,为字符串类型,最大长度为5个字符,不允许为空
	username varchar(5) not null,
	-- 创建存储 密码 的字段,固定长度 32位字符,不允许为空
	password char(32) not null,
	-- 创建 年龄字段 ,不允许为空,默认值是20
	age tinyint not null default 20
)engine=innodb default charset=utf8;
```

create table if not exists 表名(字段1 类型,字段2 类型);

```mysql
create table if not exists users(
	id int not null primary key auto_increment,
	name varchar(4) not null,
	age tinyint,
    sex enum('男', '女')
)engine=innodb default charset=utf8;
```

#### **删除表**

```mysql
# 删除users 表
drop table users;
```

#### **表结构**

```mysql
# 查看表结构
desc users;
```

#### **查看建表语句**:

```mysql
# 查看建表语句
show create table users;
```

#### 修改表结构

> 语法格式: alter table 表名 action(更改的选项)

##### 1. 添加字段

```mysql
# 语法 :alter table 表名 add 添加的字段信息

-- 在users表中 追加一个num字段
alter table users add num int not null;

-- 在指定字段后面追加字段 (eg:在users表中 age字段后面,添加一个email字段)
alter table users add email varchar(50) after age;

-- 在表的最前面添加一个字段
alter table users add phone int first;
```

##### 2. 删除字段

```mysql
# 删除字段 alter table 表名 drop 被删除的字段名
alter table users drop phone;
```

##### 3.修改字段

```mysql
语法格式: alter table 表名 change |modify 被修改的字段信息
change:可以修改字段名
modify:不能修改字段名
# 修改表中的num字段类型,使用modify不修改表名
alter table users modify num tinyint not null default 12;

# 修改表中的num字段为int 并且字段名为nn
alter table users change num mm int;

# 注意:一般情况下特殊要求,不要轻易修改表结构
```

#### 修改表名

```mysql
# 语法:alter table 原表名 rename as 新表名;
```

#### 更改表中的自增的值

```mysql
# 在常规情况下,auto_increment 默认从1开始继续递增
alter table users auto_increment = 1000;
```

#### 修改表引擎

```mysql
# 推荐在定义表时,表引擎为innodb
# 通过查看见表语句获取当前的表引擎
show create table 表名;
 users | CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(4) NOT NULL,
  `age` tinyint DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8

# 直接查看当前表状态信息 (python4是库名,users是表名)
show table status from python4 where name='users'\G;  # \G可以让输出格式化
           
           Name: users
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 2
 Avg_row_length: 8192
    Data_length: 16384
    Create_time: 2021-11-06 23:17:16
...

# 修改表引擎语句
alter table users engine = 'myisam';
```



### 6.数据操作(增删改查)

#### 插入 

```mysql
insert into 表名(字段1,字段2,字段3) values(值1,值2,值3);
# 批量添加数据
insert into 表名(字段1,字段2,字段3) values(a值1,a值2,a值3),(b值1,b值2,b值3);
# 不指定字段,这时的值,有几个字段就要填几个字段对应的值
insert into 表名 values(值1,值2,值3);  
```

#### 查询

```mysql
[where 搜索条件]
[group by 分组字段 [having 分组条件]]
[order by 排序字段 排序规则]
[limit 分页参数]
```

##### 基础查询

```mysql
# 查询表中所有列,所有数据
select * from users;

# 指定字段列表进行查询
select id,name,phone from users;
```

##### Where 条件查询

- 可以在where 子句中指定任何条件
- 可以使用and 或者or 指定一个或多个条件
- where条件也可以运用在update 和delete语句
- where子句类型程序语言中if条件,根据MySQL表中的字段来进行数据过滤

```mysql
-- 查询users表中age>22的数据
select * from users where age>22;

-- 查询users表中name=某个值的数据
select * from users where name='王五';

-- 查询年龄在22到26之间的数据
select * from users where age>=22 and age<=26;

-- 查询年龄不在22到26之间的数据
select * from users where age >22 or age>26;

-- 查询年龄在22到26之间的女生信息
select * from users where age>=22 and age<=26 and sex='女'
```

###### **and 和or 使用时注意**

假设要求查询 users表中,年龄为22 或25的女生信息

```mysql
select * from users where age=22 or age=25 and sex='女';
-- 实际查询结果并不符合要求
-- 问题出在sql计算的顺序上,sql会优先处理and条件,所以上面的sql语句就变成了
-- 查询变成了:年龄22的不管性别,或者年龄为25的女生

-- 如何改造sql符合我们的查询条件?  a:使用小括号来关联相同的条件
select * from users where (age=22 or age=25) and sex='女';
```

###### **Like子句**

> 我们可以在where条件中使用=,<,>等符合进行条件的过滤,但是当想查询某个字段是否包含时如何过滤?
>
> 可以使用like语句进行某个字段的模糊搜索
>
> 例如:查询name字段中包含五的数据

```mysql
-- like语句 某个确定的值,和 where name = '王五' 是一样的
select * from users where name like '王五';

-- 使用% 模糊搜索,%代表任意个任意字符
select * from users where name like '%五%';
-- 查询name字段中最后一个字符为'五' 的
select * from users where name like '%五';

-- 使用 '_' 单个下划线,表示一个任意字符,使用和%类似
-- 查询表中 name字段为两个字符的数据
select * from users where name like '__';
-- 查询name字段最后为'五'的两个字符的数据
select * from users where name like '_五';
```

注意:where子句中的like在使用% 或者_进行模糊搜索时,效率不高,使用时注意:

- 尽可能的不去使用%或者_
- 如果需要使用,也尽可能不要把通配符放在开头处

##### Mysql中的统计函数(聚合函数)

`max()`,` min()`, `count()`, `sum()`, `avg()`

```mysql
# 计算users表中 最大年龄,最小年龄,年龄和,以及平均年龄
select max(age),min(age),sum(age),avg(age) from users;
-- 上面数据中的列都是在查询时使用的函数名,不方便阅读和后期调用,可以通过别名方法
select max(age) as max_age,
min(age) as min_age,
sum(age) as sum_age,
avg(age) as avg_age,
from users;

-- 统计users表中的数据量
mysql> select count(*) from users;
+----------+
| count(*) |
+----------+
|        2 |
+----------+
1 row in set (0.35 sec)

mysql> select count(id) from users;
+-----------+
| count(id) |
+-----------+
|         2 |
+-----------+
-- 上面的两个统计,分别使用了count(*) 和 count(id),结果目前都一样,有什么区别?
count(*) 是按照users表中所有的列进行数据的统计,只要其中一列上有数据就可以计算
count(id)是按照指定的id字段进行统计,也可以使用别的字段进行统计,但是注意,如果指定的列上出现了NULL值,那么为NULL的这个数据不会被统计
```

##### Group by 分组

> group by 语句根据一个或多个列对结果集进行分组
>
> 一般情况下,是用与数据的统计或计算,配合聚合函数使用

```mysql
-- 统计users表中 男女生人数,根据男女生字段进行分组统计
select count(*) from users where sex='女';
select count(*) from users where sex='男';
-- 可以使用分组统计
select sex,count(*) from users group by sex;
+------+----------+
| sex  | count(*) |
+------+----------+
| 女   |        1 |
| 男   |        2 |
+------+----------+

-- 统计1班和2班的人数
select classid,count(*) from users group by classid;

-- 分别统计每个班级的男女生人数
select classid,sex,count(*) as num from users group by classid,sex;
+---------+------+-----+
| classid | sex  | num |
+---------+------+-----+
|       1 | 女   |   1 |
|       2 | 男   |   2 |
+---------+------+-----+

# 注意,在使用group by分组时,一般除了聚合函数,其他在select后面出现的字段列都需要出现在group by 后面
```

having子句

> having时在分组聚合计算后,对结果再一次进行过滤,类似where
>
> where过滤的是行数据,having过滤的是分组数据

```mysql
-- 要统计的班级人数
select classid,count(*) from users group by classid;

-- 统计班级人数,并且要人数达到4人及以上
select classid,count(*) as num from users group by classid having num>=4;
```





##### Order by 排序

> 我们在mysql中使用select的语句查询的数据结果是根据数据在底层文件的结构来排序的
>
> 首先不要依赖默认的排序,另外在需要排序时要使用order by对返回的结果进行排序
>
> asc 升序,默认
>
> desc 降序

```mysql
-- 按照年龄对结果进行排序,从大到小
select * from users order by age desc;

-- 按照从小到大排序,默认就是
select * from users order by age;

-- 也可以按照多个字段进行排序
select * from users order by age,id; # 先按照age排序,age相同时,按照id进行排序
```

##### Limit 数据分页

- limit n 	 	提取n条数据
- limit m,n      跳过m条数据,提取n条数据

```mysql
-- 查询uses表中的数据,只要3条
select * from users limit 3;

-- 跳过前4条数据,再取3条数据
select * from users limit 4,3;

-- limit 一般应用再数据分页上面
-- 例如,每页显示10条数据,第三页的limit应该怎么写?
第一页 limit 0,10
第二页 limit 10,10
第三页 limit 20,10
第四页 limit 30,10

-- 提取users表中年龄最大的三个用户数据
select * from users order by age desc limit 3;

```

##### 总结

> mysql中的查询语句比较灵活多样,所以需要多加练习,
>
> 并且在使用查询语句时,一定要注意sql的正确性和顺序

| 子句     | 说明                           | 是否必须           |
| -------- | :----------------------------- | ------------------ |
| select   | 要返回的列或表达式,字段列表\|* | 是                 |
| from     | 查询的数据表                   | 需要在表中查询时   |
| where    | 数据行的过滤                   | 否                 |
| group by | 分组                           | 仅在分组聚合计算时 |
| having   | 分组后的数据过滤               | 否                 |
| order by | 输出排序                       | 否                 |
| limit    | 要提取的结果行数               | 否                 |



#### 修改

```mysql
update 表名 set 字段=修改后值 where 条件;
update 表名 set 字段1=修改后值,字段2=修改后值 where 条件;
```

#### 删除

```mysql
delete from 表名 where 字段=某个值;
```

## Mysql的数据类型

### 1.字符串数据类型

最常用的数据类型是串数据类型,他们存储串,如名字,地址,电话号码,邮编

不管使用各种形式的串数据类型,串值都必须括在引号内

有两种基本的串类型,分别为定长串和变长串

- 定长串 CHAR

  1. 接受长度固定的字符串,其长度是在创建表时指定的,定长列不允许存储多于指定长度字符的数据
  2. 指定长度后,就会分配固定的存储空间用于存放数据

  ```
  char(7) 不管实际插入多少字符,它都会占用7个字符位置
  ```

- 变长串 VARCHAR

  存储可变长度的字符串

  ```
  varchar(7) 如果实际插入4个字符,那么它只占4个字符位置,当然插入的数据长度不能超过7个字符
  ```

注意:

```
既然变长数据类型这样灵活,为什么还要使用定长数据类型?

回答:因为性能,Mysql处理定长列远比处理变长列快得多
```

| 类型       | 大小                  | 用途                            |
| :--------- | :-------------------- | :------------------------------ |
| CHAR       | 0-255 bytes           | 定长字符串                      |
| VARCHAR    | 0-65535 bytes         | 变长字符串                      |
| TINYBLOB   | 0-255 bytes           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255 bytes           | 短文本字符串                    |
| BLOB       | 0-65 535 bytes        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535 bytes        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215 bytes    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215 bytes    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295 bytes | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295 bytes | 极大文本数据                    |

### 2.数值类型

和字符串不一样,数值不应该括在引号内

| TINYINT      | 1 Bytes                                  | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| :----------- | :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| SMALLINT     | 2 Bytes                                  | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 Bytes                                  | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 Bytes                                  | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 Bytes                                  | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 Bytes                                  | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 Bytes                                  | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |
| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |

```
decimal(5, 2) 表示数值总共5位数,小数占2位

tinyint 1字节(8位)     0-255      -128,127

int		4字节			-21亿,21亿    0-42亿

float

Mysql中没有专门存储货币的数据类型,一般情况下使用DECIMAL(8, 2)
```

#### 有符号或无符号

所有数值数据类型(除BIT和BOOLEAN外)都可以有符号或无符号

- 有符号数值列可以存储正或负的数值
- 无符号数值列只能存储正数
- 默认情况下为有符号,但如果你知道自己不需要存储负值,可以使用UNSIGNED关键字

```
类似01234存储为数值类型,则保存的将是1234,所以这样的数据要使用字符串类型存储
```

### 3.日期和时间类型 

| 类型      | 大小 ( bytes) | 范围                                                         | 格式                | 用途                     |
| :-------- | :------------ | :----------------------------------------------------------- | :------------------ | :----------------------- |
| DATE      | 3             | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| TIME      | 3             | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1             | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8             | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| TIMESTAMP | 4             | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

## 表的字段约束

create table stu(name varchar(4));

- unsigned 无符号(给数值类型使用,表示为正数,不写可以表示正负数都可以)

```
score int unsigned # 分数只能是正数
```

- 字段类型后面加括号限制宽度
  - `char(5)` ,`varchar(6)`在字符类型后面加限制,表示字符串长度
  - `int(4)`没有意义,默认无符号的int为int(11),有符号的int(10)
  - `int(4) unsigned zerofill` 只有当给int类型设置有前导零时,设置int的宽度才有意义

- `not null` 不能为空,在操作数据库时如果输入该字段的数据为NULL,就会报错
- `default` 设置默认值
- `primary key` 主键不能为空,且唯一,一般和自动递增一起配合使用
- `auto_increment` 定义列自增属性,一般用于主键,数值会自动加1
- `unique` 唯一索引(数据不能重复:用户名)可以增加查询速度,但是会降低插入和更新速度

## Mysql运算符

- 算数运算符: `+`, `-` ,`*`, `/` ,`%`

- 比较运算符:`=` ,`>`, `<` ,`>= `, `<=` ,`!=`

- 数据库特有的比较:`in`, `not in`, `is null`, `is not null`, `like`, `between`, `and`

- 逻辑运算符: `and` `or` `not`

- like: 支持特殊符号 `% ` 和 `_` ;

  ```mysql
  其中%表示任意数量的任意字符,_表示任意一位字符
  select * from users where name like '%三'  # 张三,张小三 只要是三结尾的都可以匹配到
  select * from users where name like '_三'  # 张三, 只能匹配到以三结尾且前面只有一个字符的
  ```

## 主键

1. **表中每一行都可以有唯一标识自己的一列**,用于记录两条记录不能重复,任意两行都不具有相同的主键值
2. 应该总是定义主键,虽然并不总是都需要主键,但大多数数据库设计人员都应保证他们创建的每个表具有一个主键,以便于以后的数据操纵和管理

**要求**

- 记录一旦插入到表中,主键最好不要再修改
- 不允许 NULL
- 不在主键列中使用可能会更改的值

```
例如:如果使用一个名字作为主键以标识某个供应商,当该供应商合并和更改其名字时,必须更改这个主键
```

- 自增整数类型: 数据库会在插入数据时自动为每一条记录分配一个自增整数,这样我们就完全不用担心主键重复,也不用自己预先生成主键
- 可以使用多个列作为联合主键,但联合主键并不常用,使用多列作为主键时,所有列值的组合必须是唯一的

## Mysql数据导入导出和和授权

### 数据导出

#### 1.数据库数据导出

```mysql
# 1. 不要进入mysql,然后输入以下命令导出某个库中的数据
mysqldump -uroot -p 库名 > E:\库名.sql

```

导出一个库中所有数据,会形成一个建表和添加语句组成的sql文件

之后可以用这个sql文件到别的库,或者本机中创建或恢复这些数据

#### 2.将数据库中的表导出

```
# 不要进入mysql ,然后输入以下命令,导出某个库中指定的表的数据
mysqldump -uroot -p 库名 表名 > E:\库名_表名.sql
```

### 数据导入

把导出的sql文件数据导入到mysql数据库中

```mysql
# 在新的数据库中 导入备份的数据,导入导出的sql文件
mysql -u root -p 要导入的库名< E:\库名.sql

# 把导出的表sql导入数据库
mysql -u root -p 要导入的库名< E:\库名_表名.sql
```

### 权限管理

> mysql中的root用户是数据库中权限最高的用户,千万不要用在项目中,
>
> 可以给不同的用户,或者项目,创建不同的mysql用户,并适当的授权,完成数据库的相关操作
>
> 这样就一定程度上保证了数据库的安全

创建用户的语法格式:

`grant 授权的操作 on 授权的库.授权的表 to 账户@登录地址 identified by '密码'`

示例

```mysql
# 在mysql中 创建一个zhangsan 用户,授权可以对python4这个库中所有的表 进行 添加和查询的权限
grant select,insert on python4.* to zhangsan@'%' identified by '123456';

# 用户lisi,密码123456,拥有所有权限
grant all on python4.* to lisi@'%' identified by '123456';

# 删除用户
drop user 'lisi'@'%';
```

# Python操作Mysql

mysql数据库可以应用于多种编程语言,包括PHP,Java,Go

不同编程语言操作Mysql,都是使用了mysql提供的API接口.

如果直接操作Mysql提供的API相对复杂一些,因为不同的编程语言都有不同的封装相关操作.

在python中也有很多的包或模块进行mysql数据库的操作,比较知名的包包括pymysql,mysqldb

## 安装pymysql

pip install pymysql

## 操作步骤



```python
# coding:utf-8


import pymysql

# 1.连接mysql数据库
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='python4',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    # 2.创建游标对象
    cursor = db.cursor()

    # 3.准备sql语句
    sql1 = 'insert into users(name,age,sex,classid) values("小a",32,"女",1)'
    sql2 = 'select * from users'
    sql3 = 'delete from users where id=1'
    # 4. 执行sql语句, 返回行数
    row = cursor.execute(sql1)
    # 5.提交数据 在添加修改删除时,需要commit, 如果只是查询的话,可以不用
    db.commit()
    # 6.提取结果 fetchall() 提取所有的结果, fetchone() 提取一条结果
    # 如果不是查询类sql的话,则没有返回的结果
    data = cursor.fetchall()
    # 7.关闭游标对象
    cursor.close()
except Exception as e:
    db.rollback()  # 当代码出现错误时,进行回滚
    print(e)
finally:
    # 8.关闭数据库连接
    db.close()
```

# web版的在线留言板

```
1.先实现web的基本搭建
2.创建留言板数据库
3.完成留言板的逻辑代码
```

## 1. flask框架实现web的基本搭建

### 1.1 安装flask框架

`pip install flask`

### 1.2 使用flask框架搭建web

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"

@app.route('/love')
def love():
    return 'i love you!'

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=8080)
```

## 2. 留言板数据库的设计与创建

需要创建一个templates的文件夹,存放html页面

