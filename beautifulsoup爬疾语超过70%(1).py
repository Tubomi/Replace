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


#==============================================������============================================#


def danren():
    panduan=0
    global bangadress,bangname#,key
    
    for line1 in dib:
        page=dib[line1].strip()

        url='http://bang.tx3.163.com'+str(page)      
        try:
            request = urllib2.Request(url=url,headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
                                      )#�趨��ַ�������header
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
##            pattern=re.compile(r'<span .*?>(.*?)</span>')#</li>')#ȡװ����
            pattern=re.compile(r'<li><span>(.*?)</span>(.*?)</li>',re.S)#������ֵ����
            shuxingshuzhi=re.findall(pattern,content)
            for line in shuxingshuzhi:
                aa=line[0].strip()
                bb=line[1].strip()                
                if aa==u'����':
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
#==============================================��ȫ����================================================#
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

    #======�������Ͱ��ַ����Ϊ��======#
    for line in rank1:
        renwuxinxi=line.find_all('td')
        paiming=renwuxinxi[0].text#����
        name=line.find('a').getText()#����
        namebang=line.find('a')['href']#���ַ
        fuwuqi=renwuxinxi[3].text#������
        dengji=renwuxinxi[4].text#�ȼ�
        menpai=renwuxinxi[5].text#����
        shili=line.find('a').findNext('a').getText()#������
        shilibang=line.find('a').findNext('a')['href']#������
        xiuwei=renwuxinxi[7].text#��Ϊ
        zhuangping=renwuxinxi[8].text#װ��
        zongxiuwei=renwuxinxi[9].text#����Ϊ

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
        

    #======����һҳ����======#
    nextpage=soup.find('div',attrs={'class':'dPages'})
    nextpage1=nextpage.find_all('a')
    for line in nextpage1:
        xiayiye=str(line['href'])
        xiayiyehanzi=line.text
        if xiayiyehanzi==u'��һҳ':
            bangpage=xiayiye                
            DOWNLOAD_URL='http://bang.tx3.163.com'+bangpage


with open('���а��뼲��.txt','w') as f:        
    while DOWNLOAD_URL:
        time.sleep(2)
        
        if DOWNLOAD_URL not in dia:
            dia[DOWNLOAD_URL]=1
        else:        
            break
        
        if 'page' not in DOWNLOAD_URL:
            print '��ѯ��1ҳ������...'
        if 'page' in DOWNLOAD_URL:
            page=DOWNLOAD_URL.split('page=')[1].split('&')[0]
            print '��ѯ��'+page+'ҳ������...'
            
            
        html = download_page(DOWNLOAD_URL)
        parsehtml(html)
        
        dib=dict(zip(xingminglist,banglist))#������list�ϲ���һ��dict
        did=dict(zip(xingminglist,equiplist))
##        for line in range(len(paiminglist)):
##            if paiminglist[line] not in die:
##                die[paiminglist[line]]=xingminglist[line]
##            print xingminglist[line],paiminglist[line],equiplist[line]

##        print paiminglist
        danren()

