# coding:utf-8
import requests

# url = "https://www.baidu.com"
url = 'https://www.89ip.cn/'
# 定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
res = requests.get(url, headers=headers)

code = res.status_code

print(code)

if code == 200:
    with open(".test.html", 'w', encoding="utf-8") as fp:
        fp.write(res.text)