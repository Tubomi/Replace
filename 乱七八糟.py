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
