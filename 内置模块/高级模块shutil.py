# coding:utf-8

import shutil

# copy 复制文件,把一个文件拷贝到指定的目录中,同时可以更改名字
shutil.copy('./data.json', './bb/da.json')

# copy2 和copy方法一样,可以把拷贝文件到指定目录,保留了原文件的信息(操作时间和权限等)

# copyfile 拷贝文件的内容 (打开文件,读取内容,写入到新的文件中)

# copytree 可以把整个目录结构和文件全部拷贝到指定目录中,但是要求目标目录必须不存在
shutil.copytree('./bb', './cc') # 将bb文件夹下的所有文件,拷贝到cc文件夹下

# rmtree() 删除整个文件夹
shutil.rmtree('./cc')

# move 移动文件或文件夹递归移动到另一个位置,
# shutil.move('./bb/ce/data.txt', './')