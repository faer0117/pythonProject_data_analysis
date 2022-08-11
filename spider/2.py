import urllib.request
# 下载一张图片
url_image = 'https://img1.baidu.com/it/u=1774518103,4024041627&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500'
urllib.request.urlretrieve(url_image,'image.jpg')
print("下载完成")

