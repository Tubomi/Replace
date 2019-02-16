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
__________________________________________________________________________________________
pd.set_option('display.max_rows',None)#通过修改max_rows or max_columns确定展示的行，列最大值，NONE表示显示所有内容修改数值确定最大展示行/列数
pd.set_option('display.width', 200) 显示单列全部内容，200为展示最大字符数
——————————————————————————————————
import numpy as np
import pandas as pd
date=pd.read_excel('E:\\2018\\订阅\\二月订阅\\文件名.xls',\
                  sheet_name='sheet0')
offer=date['OfferID']
offerid=[输入offerID]
name=[输入要替换的内容]#注意需一一对应
for i in range(len(name)):
    offer=offer.replace(offerid[i],name[i])
date['Offer']=pin
total=np.sum([date['计费数'],date['续订数']],axis=0)
date['后台计费数']=total
dates=date[date['Offer'].isin([想要取得的关键字])]
dates=dates[['时间','Offer','运营商','订阅数','后台计费数']]
dates=dates[dates['运营商'].isin([想要取得的关键字])]
dates=dates.groupby(['Offer','运营商']).sum()
#ping=ping.groupby('时间').sum()
dates.to_excel('E:\\2018\\订阅\\二月订阅\\12-20.xls',\
                  sheet_name='sheet0')文件名
