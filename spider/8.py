import urllib.request

# 爬取豆瓣，首页（前20的电影数据）

url ='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

fp = open('douban.json','w',encoding='utf-8')

fp.write(content)

print('打印完成')