import requests, lxml


url = "https://fanyi.baidu.com/sug"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

# post发送的数据
data = {'kw': '你好'}
res = requests.post(url=url, headers=headers, data=data)

code = res.status_code
if code ==200:
    print('请求成功')
    data = res.json()
    if data['errno'] ==0:
        print('响应成功')
        print(data['data'][0]['k'])
        v = data['data'][0]['v']
        print(v.split(';').pop())

# print(res.text)  # 返回的json数据
print(res.json())

