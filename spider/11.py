import urllib .request


def gettext():
    url ='https://meiriyiwen.com/random'

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
    }

    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    # 解析网页源码、获取想要的数据
    from lxml import etree

    tree = etree.HTML(content)

    article_list = tree.xpath('//*[@id="article_show"]')

    for i in article_list:
        article_dict = {}
        article_dict['title']=i.xpath('./h1/text()')[0]
        article_dict['author']=i.xpath('./p/span/text()')[0]
        list = i.xpath("./div[@class='article_text']/p/text()")
        text_str=''
        for i in list:
            text_str = text_str + str(i)
        article_dict['text']=text_str
        # print(article_dict)
    return article_dict


# 写入
def text_create(msg):
    # print(msg)
    # 文章保存的地址
    path = 'E:/passage/'
    desktop_path = path # 新创建的txt文件的存放路径
    full_path = desktop_path +'《' +msg['title'] + '》'+'——作者：'+msg['author']+'.doc'
    with open(full_path,'a')as f:
        f.write('《' +msg['title'] + '》'+'\r')
        f.write('————'+msg['author']+'\r')
        f.write(msg['text'])

# 睡眠函数，防止被封ip
import time
import random
def random_sleep(mu=1, sigma=0.4):
    '''正态分布随机睡眠
    :param mu: 平均值
    :param sigma: 标准差，决定波动范围
    '''
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)
    print('休眠时间为：'+str(secs))


if __name__ == '__main__':
    page_num = int(input("输入爬取文章的篇数："))
    for x in range(page_num):
        article_dict = gettext()
        text_create(article_dict)
        random_sleep()


