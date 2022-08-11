import csv
import json
import urllib.request
import urllib.parse

# 爬取豆瓣电影前250
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'

    data ={
        'start':(page-1)*20,
        'limit':20
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
    }
    data = urllib.parse.urlencode(data)

    url = base_url+data


    request = urllib.request.Request(url=url,headers=headers)

    return request


def getcontent(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content


def down_load(content):
    list = []

    for i in json.loads(content):
        moive = {}
        moive['电影名称'] = i['title']
        moive['类型'] = ','.join(i['types'])
        moive['上映日期']=i['release_date']
        moive['评价数'] = i['vote_count']
        moive['评分']=i['score']
        moive['主演'] = ','.join(i['actors'])
        list.append(moive)
    print(list)
    return list


def save_soure(header, list):
    with open('moive_data.csv','a',encoding='utf-8-sig',newline='')as f:
        w = csv.DictWriter(f,header)
        w.writeheader()
        w.writerows(list)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束的页码"))
    for page in range(start_page ,end_page+1):
        # 定制每一页的请求
        request = create_request(page)
        # 获取网页数据
        content = getcontent(request)
        # 清洗数据
        list = down_load(content)
        # 定制表头
        header = ['电影名称','类型','上映日期','评价数','评分','主演']
        # 写入csv文件中
        save_soure(header,list)
