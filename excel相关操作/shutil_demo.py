'''
1.键盘输入一个路径
2.获取里面所有的mp4文件
3.重命名mp4文件在每个文件前面添加前缀，前缀就是文件最后修改的年月日（如：2021-03-31_西游记01.mp4）
4.新建文件夹：最新视频
5.将重命名的视频批量移动到最新视频文件夹
'''
import os, datetime, shutil, glob

path = input('请输入要查询的路径：')
os.chdir(path)

if not os.path.exists('最新视频'):
    os.mkdir('最新视频')

for dirpath, dirname, files in os.walk('./'):
    for file in os.scandir(dirpath):
        if file.name.endswith('.mp4'):
            tm = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            new_file = str(tm.year) + '-' +str(tm.month)+ '-'+ str(tm.day)+'-'+file.name
            os.rename(dirpath+ '/'+ file.name, new_file)

file_ls = glob.glob('*.mp4')
for name in file_ls:
    shutil.move(name,'最新视频/')
print('over')