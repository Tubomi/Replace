# -*- coding:cp936 -*-
import urllib
import urllib2

import codecs,time

import requests,re,json,sys
from bs4 import BeautifulSoup

tp=sys.getfilesystemencoding()
dia={}
dib={}
dic={}
did={}
die={}
lista=[]
DOWNLOAD_URL = 'http://bang.tx3.163.com/bang/ranks?school=&order_key=equ_xiuwei&server='


#==============================================跑属性============================================#


def danren():
    panduan=0
    global bangadress,bangname#,key
    
    for line1 in dib:
        page=dib[line1].strip()

        url='http://bang.tx3.163.com'+str(page)      
        try:
            request = urllib2.Request(url=url,headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
                                      )#设定网址与浏览器header
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
##            pattern=re.compile(r'<span .*?>(.*?)</span>')#</li>')#取装评等
            pattern=re.compile(r'<li><span>(.*?)</span>(.*?)</li>',re.S)#属性数值正则
            shuxingshuzhi=re.findall(pattern,content)
            for line in shuxingshuzhi:
                aa=line[0].strip()
                bb=line[1].strip()                
                if aa==u'疾语':
                    jiyu=bb.split('%')[0]
                    if int(jiyu)>70:
                        print line1,bb
                        f.write(('%s\t'*2%(line1,bb)+'\n').encode(tp))
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason

    


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }).content
#==============================================跑全服榜单================================================#
def parsehtml(html):
    
    global bangpage,DOWNLOAD_URL,namebang
    global paiminglist,banglist,xingminglist,serverlist,schoollist,dengjilist,clanlist,clanbanglist,xiuweilist,equiplist,zongxiuweilist
    
    paiminglist=[]
    xingminglist=[]
    banglist=[]
    serverlist=[]
    schoollist=[]
    dengjilist=[]
    clanlist=[]
    clanbanglist=[]
    xiuweilist=[]
    equiplist=[]
    zongxiuweilist=[]
    
    soup=BeautifulSoup(html,'html.parser')
    rank=soup.find('table',attrs={'class':'table'})
    shuzi=re.compile(r'tr1|tr2')
    rank1=rank.find_all('tr',attrs={'class':shuzi})

    #======跑排名和榜地址及修为等======#
    for line in rank1:
        renwuxinxi=line.find_all('td')
        paiming=renwuxinxi[0].text#排名
        name=line.find('a').getText()#姓名
        namebang=line.find('a')['href']#榜地址
        fuwuqi=renwuxinxi[3].text#服务器
        dengji=renwuxinxi[4].text#等级
        menpai=renwuxinxi[5].text#门派
        shili=line.find('a').findNext('a').getText()#势力名
        shilibang=line.find('a').findNext('a')['href']#势力榜
        xiuwei=renwuxinxi[7].text#修为
        zhuangping=renwuxinxi[8].text#装评
        zongxiuwei=renwuxinxi[9].text#总修为

        if paiming not in paiminglist:
            paiminglist.append(paiming)
            xingminglist.append(name)
            banglist.append(namebang)
            serverlist.append(fuwuqi)
            schoollist.append(menpai)
            dengjilist.append(dengji)
            clanlist.append(shili)
            clanbanglist.append(shilibang)
            xiuweilist.append(xiuwei)
            equiplist.append(zhuangping)
            zongxiuweilist.append(zongxiuwei)
        else:
            continue
        

    #======跑下一页链接======#
    nextpage=soup.find('div',attrs={'class':'dPages'})
    nextpage1=nextpage.find_all('a')
    for line in nextpage1:
        xiayiye=str(line['href'])
        xiayiyehanzi=line.text
        if xiayiyehanzi==u'下一页':
            bangpage=xiayiye                
            DOWNLOAD_URL='http://bang.tx3.163.com'+bangpage


with open('排行榜与疾语.txt','w') as f:        
    while DOWNLOAD_URL:
        time.sleep(2)
        
        if DOWNLOAD_URL not in dia:
            dia[DOWNLOAD_URL]=1
        else:        
            break
        
        if 'page' not in DOWNLOAD_URL:
            print '查询第1页内容中...'
        if 'page' in DOWNLOAD_URL:
            page=DOWNLOAD_URL.split('page=')[1].split('&')[0]
            print '查询第'+page+'页内容中...'
            
            
        html = download_page(DOWNLOAD_URL)
        parsehtml(html)
        
        dib=dict(zip(xingminglist,banglist))#将两个list合并成一个dict
        did=dict(zip(xingminglist,equiplist))
##        for line in range(len(paiminglist)):
##            if paiminglist[line] not in die:
##                die[paiminglist[line]]=xingminglist[line]
##            print xingminglist[line],paiminglist[line],equiplist[line]

##        print paiminglist
        danren()

