import urllib.request
import urllib.parse
# 解码2

url ='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

# 将中文解码成unicode形式
data= {
    'wd' : '周杰伦',
    'sex' : '男',
    'location':'中国台湾省'
}

# 生成unicode形式的查询条件
new_data = urllib.parse.urlencode(data)

# 拼接url
url = url+new_data

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)