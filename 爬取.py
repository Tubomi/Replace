from bs4 import BeautifulSoup as bs
import requests
# urllib.request
import re
import json
#import json2html
import pandas as pd
import time
import random
df=pd.DataFrame({},columns=['time', 'title',"content"])
df.to_excel('E:\\个人\\test.xls',sheet_name='sheet0')
def _request(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    proxies = { "http": "http://114.239.150.199", } 
    res=requests.get(url,headers=headers,proxies=proxies)
    soup=bs(res.content,'lxml',from_encoding='utf-8')
    return soup
def time_sleep():
    sleep=random.random()*3
    time.sleep(sleep)
    
def get_link(urls):
    for i in urls:
        
        print("正在读取"+str(i))
        essaylink=_request(i)
        get_contentlinks(essaylink)
        #get_pagetracklink(self._request(i))
        time_sleep()
                
def get_page(page):
    for i in range(page):
        url="https://book.douban.com/people/80348933/annotation/?start="
        s=i*5
        url=url+str(s)
        pagelinks=_request(url)
        time_sleep()
        get_tracklinks(pagelinks)
def get_tracklinks(soup):
    cont=soup.find_all('h3')
    recom=re.compile(r'<a href="(.*?)" title.*?', re.S)
    respone=re.findall(recom,str(cont))
    essay_links=get_link(respone)
def get_contentlinks(soup):
    cont1=soup.find_all('h5')
    recom=re.compile(r'<a href="(.*?)">', re.S)
    respone=re.findall(recom,str(cont1))

    for i in respone:
        print("正在爬取"+str(i))
        reply=_request(i)
        time_sleep()
        get_content(reply)
def get_content(soup):
    cont2=(soup.find('pre',id="link-report")).string
    title=(soup.find('h1')).string
    time=soup.find('span',class_="pubtime").string
    all_comment=pd.read_excel('E:\\新建文件夹\\test.xls',sheet_name='sheet0')
    s=({'time':time,'title':title,'content':cont2})
    comments=all_comment.append(s, ignore_index=True)  

    comments.to_excel('E:\\新建文件夹\\test.xls',sheet_name='sheet0')
    time_sleep()
    print("读取完毕")
    
