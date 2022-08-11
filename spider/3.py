import urllib.request
# 下载一张图片
url_vide= 'http://v26-web.douyinvod.com/fadd4c84ca2850e14177e868b4ef8697/62de6557/video/tos/cn/tos-cn-ve-15c001-alinc2/90433a6d9f7a438b944aa61993686e6d/?a=6383&amp;ch=5&amp;cr=3&amp;dr=0&amp;lr=all&amp;cd=0%7C0%7C0%7C3&amp;cv=1&amp;br=1344&amp;bt=1344&amp;cs=0&amp;ds=3&amp;ft=X1nbLXvvBQiAUEuyJ8Z.BOMzJ4lc9TL6F2bL4oWy0DZm&amp;mime_type=video_mp4&amp;qs=0&amp;rc=N2U1NTg5Zzc2ZGdmNDVoZkBpanFqaDU6Zm5yZTMzNGkzM0AzYGEtYjAzXjIxYDMxMDFhYSNfbXBmcjRvYTRgLS1kLS9zcw%3D%3D&amp;l=202207251639160102040502054201A33A'
urllib.request.urlretrieve(url_vide,'vide_test.mp4')
print("下载完成")

