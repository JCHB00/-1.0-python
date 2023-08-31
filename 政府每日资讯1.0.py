#政府每日资讯1.0.py
#于2022/9/3 完成
#轩

#模组区
import requests
import re
import chardet
import json
from lxml import etree

#变量区
words = None
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"}


#函数区

#'''香港政府新闻'''
url = 'https://www.info.gov.hk/gia/general/ctoday.htm'

html = requests.get(url,headers = headers)
print(chardet.detect(html.content))
html.encoding = chardet.detect(html.content)['encoding']
m = re.findall('>(.*)</a></li>',str(html.text))
print('当日新闻内容:')
for i in m:
    num = 0
    for n in i:
        num += 1
        if n =='>':
            words =i[num:]
    if words:
        print('***',words,sep="\n")
print(f'资料来原:{url}')


#'''今日疫情数据'''
url = 'https://chp-dashboard.geodata.gov.hk/covid-19/data/config-v2.json?_=1662133952891'
html = requests.get(url,headers=headers)
data_url = 'https://chp-dashboard.geodata.gov.hk/covid-19/data/keynum.json?_=1662133952892'
data_json = requests.get(data_url,headers=headers)
title = re.search('"title": "(.*)"',str(html.text))
with open('Data.json','w') as fileobj:
    json.dump(data_json.json(),fileobj)
with open('Data.json') as fnobj:
    Data = json.load(fnobj)
#输入区
print(title)
print('今日阳性个案')
print('Confirmed_Delta[核酸檢測]:',Data['Confirmed_Delta'])
print('RAT_Positive_Delta[抗原快測]:',Data['RAT_Positive_Delta'])
print(f'今日总案例：{Data["Confirmed_Delta"]+Data["RAT_Positive_Delta"]}')
print('累計個案 (核酸檢測+抗原快測): [没有该项数据]')
print(f'今日死亡人数为:{Data["Death"]-Data["P_Death"]}')
print('总死亡人数:',Data['Death'])

#天气区
print('天气区')
print('现在天气')

ans = int(input('退出请按0'))
    
