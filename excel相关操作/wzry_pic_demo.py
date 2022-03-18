'''
1.下载王者荣耀高清壁纸图片
2.将不同人物的图片分别保存到 临时文件夹
3.将不同人物的图片打包压缩成zip文件
4.移动图片到pictures文件夹
'''
import requests
from bs4 import BeautifulSoup

url01 = 'https://pvp.qq.com/web201605/wallpaper.shtml###'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50'
}
resp = requests.get(url01,headers=headers)
resp.encoding = resp.apparent_encoding
result = resp.text
print(result)
soup = BeautifulSoup(result,'lxml')
# res = soup.find_all('li', attrs={'class':'sProdImgDown sProdImgL6'})
res = soup.find_all('a')
res = soup.find_all('li', attrs={'class':'sProdImgDown sProdImgL6'},recursive=True)
print(res)

