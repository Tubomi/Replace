import numpy as np
import pandas as pd
xl=pd.read_excel('E:\\2018\\订阅\\二月订阅\\stat-subscribe-net-2018-11-19.xls',sheet_name='sheet0')
y=xl["Country"]+'_'+xl['Carrier']
xl.drop(['Country','Carrier'],axis=1,inplace=True)
xl['国家运营商']=y
x2=pd.read_excel('E:\\2018\\订阅\\二月订阅\\stat-subscribe-net-2018-11-20.xls',sheet_name='sheet0')
y1=x2["Country"]+'_'+x2['Carrier']
x2.drop(['Country','Carrier'],axis=1,inplace=True)#inplace=True 直接替代x2内容 
x2['国家运营商']=y1
z=pd.merge(xl,x2,on=['国家运营商'],suffixes=("19号","20号"))#以on的内容作为唯一匹配值，其他相同值后缀加上suffixes内的值 还没想到怎么样才能只输入一遍
n=z['Revenues20号']-z['Revenues19号']
z['收益差值']=n
z.to_excel('E:\\2018\\订阅\\二月订阅\\456.xls',sheet_name='sheet0')
