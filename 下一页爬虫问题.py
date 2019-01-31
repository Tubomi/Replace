#重点要解决的：图片和文字在一起的时候爬取为空，所以要重新改代码；
#拿到图片链接
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url='https://book.douban.com/annotation/66983789/'
    proxies = { "http": "http://114.239.150.199", } 
    ht=requests.get(url,headers=headers,proxies=proxies)
    soup=bs(ht.content,'lxml',from_encoding='utf-8')
    cont=soup.find("div",class_="image-wrapper")
    recom=re.compile(r'<img src="(.*?)" width=.*?', re.S)
    respone=re.findall(recom,str(cont))
    respone
    
******************************************************************************************************
from bs4 import BeautifulSoup as bs
import requests
# urllib.request
import re
import json
#import json2html
import pandas as pd
import time
import random
s=[]
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
def next_page(url):
    soup=_request(url)
    cont=soup.find("span",class_="next")
    recom=re.compile(r'<a href="(.*?)"w*?', re.S)
    respone=re.findall(recom,str(cont))
    #total=url+str(s)
    return respone
                     
def get_page(url):
    pagelinks=_request(url)
    pagelink=get_tracklinks(pagelinks)
    x=next_page(url)
    if x ==[]:
        print("读取全部页码完毕")
    else:
        get_page(url+str(s))

def get_tracklinks(soup):#获取每个页码内全部书的链接”
    cont=soup.find_all('h3')
    recom=re.compile(r'<a href="(.*?)" title.*?', re.S)
    respone=re.findall(recom,str(cont))
    for i in respone:    
        print("正在读取"+str(i))
        essaylink(i)
        #get_pagetracklink(self._request(i))
        time_sleep()
def essaylink(url):
    replylink=_request(url)
    get_contentlinks(replylink)
    x=next_page(url)
    if x ==[]:
        print("读取该篇文章内所有页码完毕")
    else:
        essaylink(total)
                      
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
    print("读取该书完毕")
