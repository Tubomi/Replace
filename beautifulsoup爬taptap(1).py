# -*- coding:cp936 -*-
import urllib
import urllib2

import codecs,time,datetime

import requests,re,json,sys
from bs4 import BeautifulSoup


tp=sys.getfilesystemencoding()
dia={}
dib={}
dic={}
did={}
die={}
lista=[]
DOWNLOAD_URL = 'https://www.taptap.com/app/49995/review?order=default&page=2#review-list'#'https://www.taptap.com/app/49995/review'

nowtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
yestoday=(datetime.date.today()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")


#==============================================������============================================#


##def danren():
##    panduan=0
##    global bangadress,bangname#,key
##    
##    for line1 in dib:
##        page=dib[line1].strip()
##
##        url='http://bang.tx3.163.com'+str(page)      
##        try:
##            request = urllib2.Request(url=url,headers={
##                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
##                                      )#�趨��ַ�������header
##            response = urllib2.urlopen(request)
##            content = response.read().decode('utf-8')
####            pattern=re.compile(r'<span .*?>(.*?)</span>')#</li>')#ȡװ����
##            pattern=re.compile(r'<li><span>(.*?)</span>(.*?)</li>',re.S)#������ֵ����
##            shuxingshuzhi=re.findall(pattern,content)
##            for line in shuxingshuzhi:
##                aa=line[0].strip()
##                bb=line[1].strip()                
##                if aa==u'����':
##                    jiyu=bb.split('%')[0]
##                    if int(jiyu)>70:
##                        print line1,bb
##                        f.write(('%s\t'*2%(line1,bb)+'\n').encode(tp))
##        except urllib2.URLError, e:
##            if hasattr(e,"code"):
##                print e.code
##            if hasattr(e,"reason"):
##                print e.reason

    


def download_page(url):
    return requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'},verify=False).content
#==============================================��ȫ����================================================#
def parsehtml(html):
    
    global bangpage,DOWNLOAD_URL,namebang
    global xingminglist,shijianlist,pinglunlvlist,pingluncontentlist,pinglunmodellist
    
    xingminglist=[]
    shijianlist=[]
    pinglunlvlist=[]
    pingluncontentlist=[]
    pinglunmodellist=[]
    
    soup=BeautifulSoup(html)#,'html.parser')
    rank=soup.find('ul',attrs={'class':'list-unstyled taptap-review-list'})

    neirong=rank.find_all('li',attrs={'class':'taptap-review-item collapse in'})

    #======�ܾ�������======#
    for line in neirong:
##        try:
        xingming=line.find('a',attrs={'class':'taptap-user-name'}).text#����������
        pingluntime=str(line.find('a',attrs={'class':'text-header-time'}).text).strip()#����ʱ��
        pinglunriqi=pingluntime.split(' ')[0].strip()
        pinglunlv=str(int(str(line.find('div',attrs={'class':'item-text-score'}).find('i')).split(': ')[1].split('px')[0])/(14))#.encode(tp)#�����Ǽ�
        pingluncontent=line.find('div',attrs={'class':'item-text-body'}).text
        pingluncontent1=pingluncontent.encode(tp).strip()
        try:
            pinglunmodel=line.find('span',attrs={'class':'text-footer-device'}).text
        except:
            pinglunmodel=u'���豸��Ϣ'
##        print xingming,type(pingluncontent1)
##        if pinglunriqi<yestoday:
##            continue
        if pingluntime not in shijianlist:
            xingminglist.append(xingming)
            shijianlist.append(pingluntime)
            pinglunlvlist.append(pinglunlv)
            pingluncontentlist.append(pingluncontent1)
            pinglunmodellist.append(pinglunmodel)

    
    #======����һҳ����======#
    nextpage=soup.find('div',attrs={'class':'main-body-footer'})
    nowpage=nextpage.find('li',attrs={'class':'active'})#��ǰ�ҳ

    nowpage1=nowpage.text#��ǰ�ҳҳ��
    try:
        nextpage1=str(nowpage.findNext('a')['href'])#��һҳ��ַ
        nextpage2=nowpage.findNext('li').text#��һҳҳ��


        if str(nextpage2)=='>':
            nextpage1=DOWNLOAD_URL

    except Exception,e:
        print 1

    DOWNLOAD_URL='%s'%nextpage1#+'#review-list'



with open('taptap.txt','w') as f:        
    while DOWNLOAD_URL:
        time.sleep(2)
        
        if DOWNLOAD_URL not in dia:
            dia[DOWNLOAD_URL]=1
        else:        
            break
        
##        if 'page' not in DOWNLOAD_URL:
##            print '��ѯ��1ҳ������...'
##        if 'page' in DOWNLOAD_URL:
##            page=DOWNLOAD_URL.split('page=')[1].split('&')[0]
##            print '��ѯ��'+page+'ҳ������...'
##            
            
        html = download_page(DOWNLOAD_URL)
        parsehtml(html)

        dib=dict(zip(xingminglist,pinglunmodellist))#������list�ϲ���һ��dict
        for line in range(len(xingminglist)):
            print u'������:%s'%xingminglist[line]
            print u'����ʱ��:%s'%shijianlist[line]
            print u'�Ǽ�:%s'%pinglunlvlist[line]
            print u'�豸��Ϣ:%s'%pinglunmodellist[line]
            print '��������:%s'%pingluncontentlist[line]
            print '\n\n'


