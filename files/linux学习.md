# Linux学习

## 1.基本命令

`pwd` 查当前目录

`ll` 查看文件 ls -l 的缩写

`cd` 切换目录访问

```linux
cd / 根目录 xiaoma@ubuntu:/$   /
cd ~ 家目录 xiaoma@ubuntu:~$   /home/xiaoma
cd - 去上次的目录
```

`mkdir 目录名` 创建目录

```
mkdir ./python/b 当前目录中的python目录下创建b目录(此时python目录已存在,如不存在会报错)
mkdir -p a/b/c 递归创建目录 加-p
```

`rmdir 目录名` 删除目录

```
rmdir ./python  这个命令只能删除空目录,此时非空会报错
rm python 		python非空,也会报错
rm -r python 	-r是递归删除
rm -f python	-f强制删除,不会有任何提示
```

`cp` 复制文件或目录

```
cp b ./a 		将b文件复制到a目录
cp -r b ./a 	将b目录复制到a目录 复制目录的时候要-r递归
xiaoma@ubuntu:~/python/b/a$ cp -rv b ../../d
'b' -> '../../d/b'
'b/c' -> '../../d/b/c'
'b/c/d' -> '../../d/b/c/d'
				-v 显示复制细节
```

`mv` 移动目录或文件(更改文件名)

```
mv a ./av 将a目录移动到当前目录,并更名为av
```

`touch` 创建文件

```
touch a.txt
```

`rm` 删除文件

```
rm a.txt
```

`mv` 更改文件名

```
mv a.txt c.txt
```

`cat` `more` `less` 查看文件

```
cat a.txt  		常用
more a.txt		查看长文件 回车看下一行,空格翻页,q退出
less a.txt	    查看长文件,使用上下方向键翻看
```

`ln` 硬链接,软连接

```
ln 源文件 链接文件 		硬链接:只能链接普通文件,不能链接目录
ln -s  a   b  			软链接:类似windows中的快捷方式,此处b文件是a文件的快捷方式
```

`du` 查看文件信息

## 2.vim编辑器

## 3.其他命令

`shutdown -h now` 关机(执行时需要加sudo)

`shutdown -r now` 重启(执行时需要加sudo)

`sudo reboot` 重启

`date` 时间: 

```linux
xiaoma@ubuntu:~/python$ date
Tue 09 Nov 2021 12:36:03 PM UTC
xiaoma@ubuntu:~/python$ date "+%Y-%m-%d %H:%M:%S"
2021-11-09 12:36:59

# 设置时区为中国的时间
xiaoma@ubuntu:~/python$ sudo timedatectl set-timezone Asia/Shanghai
[sudo] password for xiaoma:
xiaoma@ubuntu:~/python$ date
Tue 09 Nov 2021 08:40:52 PM CST
```

`>`,  `>>` 重定向

```
# > 每次重定向会清空之前的内容
xiaoma@ubuntu:~/python$ echo hello > a.txt
xiaoma@ubuntu:~/python$ cat a.txt
hello
xiaoma@ubuntu:~/python$ echo world > a.txt
xiaoma@ubuntu:~/python$ cat a.txt
world

# >> 每次重定向会追加内容 
xiaoma@ubuntu:~/python$ echo hello world >> a.txt
xiaoma@ubuntu:~/python$ cat a.txt
hello world
xiaoma@ubuntu:~/python$ echo hi world >> a.txt
xiaoma@ubuntu:~/python$ cat a.txt
hello world
hi world
```

`grep` 查找

```
# 查找a.log文件中有 'b'的行
xiaoma@ubuntu:~/python$ grep 'b' a.log
drwxrwxr-x 3 xiaoma xiaoma 4096 Nov  9 18:52 b/
-rw-rw-r-- 2 xiaoma xiaoma   13 Nov  9 20:06 b.txt

# -i 不区分大小写
xiaoma@ubuntu:~/python$ grep -i 'B' a.log
drwxrwxr-x 3 xiaoma xiaoma 4096 Nov  9 18:52 b/
-rw-rw-r-- 2 xiaoma xiaoma   13 Nov  9 20:06 b.txt

# -v 查找不含'b'的内容行
xiaoma@ubuntu:~/python$ grep -v 'b' a.log
drwxrwxr-x 8 xiaoma xiaoma 4096 Nov  9 20:48 ./
drwxr-xr-x 5 xiaoma xiaoma 4096 Nov  9 19:58 ../
-rw-rw-r-- 1 xiaoma xiaoma    0 Nov  9 20:48 a.log
-rw-rw-r-- 1 xiaoma xiaoma   21 Nov  9 20:45 a.txt
drwxrwxr-x 3 xiaoma xiaoma 4096 Nov  9 18:40 av/
```

`|` 管道符

```
命令a | 命令b  		将a操作后的输出结果,交给b处理

xiaoma@ubuntu:~$ ll | grep 'pyth'
drwxrwxr-x 8 xiaoma xiaoma 4096 Nov  9 20:48 python/
```

`wc` 查看文件的行数,单词,字符

```
xiaoma@ubuntu:~$ wc /etc/ssh/sshd_config
 124  398 3316 /etc/ssh/sshd_config
行数  单词  字符  文件
```

`wget` 下载信息

```
xiaoma@ubuntu:~/python/$ wget www.baidu.com
# 将下载的网页设置a.html名
xiaoma@ubuntu:~/python/$ wget -O a.html www.baidu.com
# 指定下载到download目录中
xiaoma@ubuntu:~/python/$ wget -P download www.baidu.com
# 大文件的断点续传
xiaoma@ubuntu:~/python/$ wget -c www.baidu.com
# 后台下载
xiaoma@ubuntu:~/python/$ wget -b download www.baidu.com
```

`curl` 请求地址,并将结果返回到终端

```
curl www.baidu.com >>baidu.txt
```

## 4.文件查找

`find` 

```
# 从根目录开始查找file.log的文件
xiaoma@ubuntu:~$ sudo find / -name file.log
/home/xiaoma/python/download/O/file.log

# 不区分大小写
xiaoma@ubuntu:~$ sudo find / -iname FILE.log
/home/xiaoma/python/download/O/file.log

# 按文件大小查找
find /home/ -size 1k	home目录下文件大小为1k的文件
find /home/ -size +1k	home目录下文件大小大于1k的文件
find /home/ -size -1k	home目录下文件大小小于1k的文件

# 查小文件时,按字节查找的话,在字节数后面加c
# 当前目录查找大小为11字节的文件
find . -size 11c

# 按照文件类型查找 d-->目录 f-->文件, l->软链接
find /home/ -type l
```

`whereis`

```
xiaoma@ubuntu:~$ whereis find
find: /usr/bin/find /usr/share/man/man1/find.1.gz /usr/share/info/find.info-2.gz /usr/share/info/find.info-1.gz /usr/share/info/find.info.gz

xiaoma@ubuntu:~$ whereis -b find	# -b按照二进制文件去找
find: /usr/bin/find
```

`which` (重点)

```
xiaoma@ubuntu:~$ which find
/usr/bin/find
```

## 5.磁盘挂载

```
# 挂载
sudo mount 设备描述文件 挂载点(一般是一个空目录)

# 卸载
sudo umount 挂载点

# df 查看挂载情况命令
```

