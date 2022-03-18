import os

if os.path.exists('package01'):
    print('存在')
else:
    # 在当前目录下创建文件夹
    os.mkdir('package01')
if not os.path.exists('package02'):
    os.makedirs('package02/package03/package04')

# 删除
import shutil
# shutil.rmtree('package02')

# 复制文件
shutil.copy('os_demo3.py', 'package01')
# 复制文件夹
shutil.copytree('package01', 'package02/package001')