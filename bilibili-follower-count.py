import requests                 # 用于得到网页链接
import json                     # 用于解析JSON格式的库

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
# 储存粉丝数
response = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + '1571631329' + '&jsonp=jsonp',
                          headers=headers)
J_data = json.loads(response.text)
print(J_data['data']['follower'])




