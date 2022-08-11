import urllib.request

# 代理ip
url ='https://meiriyiwen.com/random'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# ip代理池
# proxies_pool= [
#     {'https': 'https://{}'.format('221.182.101.213:8123')}
# ]
# import random
#
#
# proxies = random.choice(proxies_pool)
#
# handler = urllib.request.ProxyHandler(proxies=proxies)
#
# opener = urllib.request.build_opener(handler)
# response = opener.open(request)


# 获取响应信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html','w',encoding='utf-8')as fp:
    fp.write(content)

