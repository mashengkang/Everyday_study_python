# 登录mysql,在终端输入一下命令,进行登录
mysql -uroot -p

# 查看当前mysql中所有的库,(库==>数据库==>就像文件夹,库里可以存储多个表
show databases;
-- +--------------------+
-- | Database           |
-- +--------------------+
-- | information_schema |
-- | mysql              |
-- | performance_schema |
-- | python-04          |
-- | python4            |
-- | python_test        |
-- | sys                |
-- +--------------------+
7 rows in set (0.01 sec)

# 查看当前库中的所有数据表
show tables;

# 查看user表中的数据
select * from user;

# 查看 user表中的所有数据的 host 和user 字段列
select host,user from user;

# 库,表
# 库就像是文件夹,库中可以有很多表


# 创建库的语法
create database 库名 default charset=utf8
# 查看库
show databases;
# 进入库
use 库名;


# 创建表的语法
create table 表名(
	字段名 类型 字段约束,
	字段名 类型 字段约束,
	字段名 类型 字段约束,
	)engine==innodb default charset=utf8;
	
create table user(
	name varchar(20),
	age int,
	sex char(1)
	)engine=innodb default charset=utf8;
	
# 添加一些数据
insert into user(name,age,sex) values('admin',26,'男');
insert into user(name,age,sex) values('张三',22,'女');
# 查看表中的数据
select * from user;


