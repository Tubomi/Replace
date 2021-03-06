#重点要解决的：图片和文字在一起的时候爬取为空，所以要重新改代码；
#rcom=re.compile(r'w*?</div><p>"(.*?)"</p></pre>', re.S)（得到图片链接）
已经爬取成功，图片地址已经爬了下来，但是没有细分。
from bs4 import BeautifulSoup as bs
import requests
# urllib.request
import re
import json
#import json2html
import pandas as pd
import time
import random
def get_url(url):
    url=str(url)
    s="?start="
    if s not in url:
        url=url.split(" ",1)
        return url
    else:
        recom=re.compile(r'(.*?)[?!].*?', re.S)
        url=re.findall(recom,str(url))
        return url
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
    recom=re.compile(r'<a href="(.*?)">.*?', re.S)
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
        url=get_url(url)
        get_page(url[0]+str(x[0]))

def get_tracklinks(soup):#获取每个页码内全部书的链接”
    cont=soup.find_all('h3')
    recom=re.compile(r'<a href="(.*?)" title.*?', re.S)
    respone=re.findall(recom,str(cont))
    for i in respone:    
        print("正在读取"+str(i))
        essaylink(i)
        print("读取该页完毕")
        #get_pagetracklink(self._request(i))
        time_sleep()
def essaylink(url):
    replylink=_request(url)
    get_contentlinks(replylink)
    x=next_page(url)
    if x ==[]:
        print("读取该篇文章内所有页码完毕")
    else:
        url=get_url(url)
        essaylink(url[0]+str(x[0]))
                      
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
    title=(soup.find('h1')).string
    time=soup.find('span',class_="pubtime").string
    cont=soup.find("pre",id="link-report")
    cont=str(cont)
    recom=re.compile(r'<p>(.*?)</p></pre>',re.S)
    cont2=re.findall(recom,cont)
    all_comment=pd.read_excel('F:\\book\\test.xls',sheet_name='sheet0')
    s=({'time':time,'title':title,'content':cont2})
    comments=all_comment.append(s, ignore_index=True)  

    comments.to_excel('F:\\book\\test.xls',sheet_name='sheet0')
    time_sleep()
    print(str(title)+"该评论读取完毕")
