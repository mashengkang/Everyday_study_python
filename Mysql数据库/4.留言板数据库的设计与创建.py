# coding:utf-8

'''
nikename 昵称 info 留言信息 datetime 留言时间
1.      张三  我想要买个彩票     2021-11-8 12:12:12


创建库
create database pymysql charset=utf8mb4;
创建表
create table lyb(
    id int unsigned not null auto_increment primary key,
    nikename varchar(6) not null,
    info text not null,
    date datetime not null
)engine=innodb default charset=utf8mb4;

添加测试数据
insert into lyb values(null,'张三丰','我想要大家帮我抢个票','2021-11-8 12:12:12');
insert into lyb values(null,'渣渣灰','是兄弟就来砍我吧','2021-11-8 12:12:12');
'''