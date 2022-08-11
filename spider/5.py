import urllib.request
# 解码

# url ='https://cn.bing.com/search?q=%E6%9E%97%E4%BF%8A%E6%9D%B0'
url ='https://cn.bing.com/search?q='

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

# 将中文解码成unicode形式
name = urllib.parse.quote('林俊杰')
# print(name)

url = url+name

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)