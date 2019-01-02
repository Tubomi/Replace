#网易iframe内嵌框架爬取 https://www.jianshu.com/p/4e96f8466261
#

from bs4 import BeautifulSoup as bs
import requests
# urllib.request
import re
import json
#import json2html
import pandas as pd
url1='https://music.163.com/djradio?id=2231010'
headers = {  
    'Cookie':'__e_=1515461191756; _ntes_nnid=af802a7dd2cafc9fef605185da6e73fb,1515461190617; _ntes_nuid=af802a7dd2cafc9fef605185da6e73fb; JSESSIONID-WYYY=HMyeRdf98eDm%2Bi%5CRnK9iB%5ChcSODhA%2Bh4jx5t3z20hhwTRsOCWhBS5Cpn%2B5j%5CVfMIu0i4bQY9sky%5CsvMmHhuwud2cDNbFRD%2FHhWHE61VhovnFrKWXfDAp%5CqO%2B6cEc%2B%2BIXGz83mwrGS78Goo%2BWgsyJb37Oaqr0IehSp288xn5DhgC3Cobe%3A1515585307035; _iuqxldmzr_=32; __utma=94650624.61181594.1515583507.1515583507.1515583507.1; __utmc=94650624; __utmz=94650624.1515583507.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=94650624.4.10.1515583507',  
    'Host':'music.163.com',  
    'Refere':'http://music.163.com/',  
    'Upgrade-Insecure-Requests':'1',  
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'  
}

ht=requests.get(url1,headers=headers)
soup=bs(ht.content,'lxml',from_encoding='utf-8')
#print(soup.prettify())
tracks=soup.find_all("div",class_="tt f-thide")
for i in tracks:
    url="https://music.163.com/"+i.a.get("href")
    print(url)
  
 
#网易翻页问题还没弄，目前只读取了第一页的各节目链接
#读取页码，其实几页直接弄就好了，正则表达式哪里需要注意一下
from bs4 import BeautifulSoup as bs
import requests
# urllib.request
import re
import json
#import json2html
import pandas as pd
url1='https://music.163.com/djradio?id=2231010'
headers = {  
    'Cookie':'__e_=1515461191756; _ntes_nnid=af802a7dd2cafc9fef605185da6e73fb,1515461190617; _ntes_nuid=af802a7dd2cafc9fef605185da6e73fb; JSESSIONID-WYYY=HMyeRdf98eDm%2Bi%5CRnK9iB%5ChcSODhA%2Bh4jx5t3z20hhwTRsOCWhBS5Cpn%2B5j%5CVfMIu0i4bQY9sky%5CsvMmHhuwud2cDNbFRD%2FHhWHE61VhovnFrKWXfDAp%5CqO%2B6cEc%2B%2BIXGz83mwrGS78Goo%2BWgsyJb37Oaqr0IehSp288xn5DhgC3Cobe%3A1515585307035; _iuqxldmzr_=32; __utma=94650624.61181594.1515583507.1515583507.1515583507.1; __utmc=94650624; __utmz=94650624.1515583507.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=94650624.4.10.1515583507',  
    'Host':'music.163.com',  
    'Refere':'http://music.163.com/',  
    'Upgrade-Insecure-Requests':'1',  
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'  
}
#proxies =｛ "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080", ｝
proxies = { "http": "http://61.135.217.78", } 
ht=requests.get(url1,headers=headers,proxies=proxies)
soup=bs(ht.content,'lxml',from_encoding='utf-8')
print("ok")
page=soup.find_all("div",class_="u-page")
recom=re.compile(r'.*? href="(.*?)">.?</a>',re.S)
respone=re.findall(recom,str(page))
for i in respone:
    print(i)
               
#99乘法表
for i in range(1,10):
    for j in range(1,10):
        print('%s*%s=%s'%(i,j,i*j),end=' ')
        if j > i:
            break
    print()
#二

import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
url='https://movie.douban.com/subject/1292052/'
r=requests.get(url).text
s=etree.HTML(r)
story=s.xpath('//*[@id="link-report"]/span[2]/text()')
#xi=re.compile('\u300020.+\n')
story[0].strip()
h=s.xpath('//*[@id="hot-comments"]/div[1]/div/p/text()')
h[0].strip()

#三

import xlrd
   
fname = "reflect.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
 sh = bk.sheet_by_name("Sheet1")
except:
 print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
#获取第一行第一列数据 
cell_value = sh.cell_value(1,1)
#print cell_value
   
row_list = []
#获取各行数据
for i in range(1,nrows):
 row_data = sh.row_values(i)
 row_list.append(row_data)
    
 #那些零零总总遇到的坑
 pycrypto不支持3.6版本，新版pip install pycryptodome
 Crypto安装后显示不存在，去Python安装库lib-setpackages找到文件 把小写改成大写

