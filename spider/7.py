import urllib.request
import urllib.parse
# 百度翻译

url ='https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Cookie':'BAIDUID=5DA2383A3A6BE8B6CF43FDFDA633117E:FG=1; BIDUPSID=5DA2383A3A6BE8B60418802783466807; PSTM=1655169059; ZFY=dpcziqT1O0LKs:AYGGMCp2:BToYjZUWE5cVl5kazLEYTM:C; H_PS_PSSID=36551_36465_36726_36413_36852_36167_36816_36569_36807_36653_36746_26350_36687; BA_HECTOR=al0h80alah208h2k8h8ltrol1hdsotu16; delPer=0; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1658743194; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1658743819; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZWFhMGE5YjkwNjhjNmU4ZTg5NTc0YzZkMzFlMzAzYjVlNzI2ZjVhNjg0ZGQ4MjE4ODIzNGZhODdkNmFlNjY3NDc2MDFlZjM3ODVmMzAxYWZiMjE1YmFhMGI4MWY0MWZmYjIwZDg1NTg1YjgzMzRjMDkxMmUwMWIyYzE4OGIzODBjMmQ2ZGEyZDY2ZDA1NjA4MjdmNjY2YTI3ZjA2NWVlNA=='

}

data = {
        'from':'zh',
        'to':'en',
        'query':'蜘蛛',
        'transtype':'realtime',
        'simple_means_flag':'3',
        'sign':'347277.110524',
        'token':'b1b77a9f99b20ca37cb86bbdc39d4185',
        'domain':'common'
}



data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
# print(content)

# 把得到的str形式数据装换成json格式
import  json

obj = json.loads(content)

print(obj)
