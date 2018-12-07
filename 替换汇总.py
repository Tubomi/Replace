import numpy as np
import pandas as pd
din=pd.read_excel('E:\\2018\\订阅\\二月订阅\\stat-subscribe-2018-11-18.xls',\
                  sheet_name='sheet0')
pin=din['OfferID']
number=[1232,4560]
name=['Y1','Y2']
for i in range(len(name)):
    pin=pin.replace(number[i],name[i])
din['Offer']=pin
total=np.sum([din['计费数'],din['续订数']],axis=0)
din['后台计费数']=total
ping=din[din['Offer'].isin(['Y1','Y2'])]
ping=ping[['时间','Offer','运营商','订阅数','后台计费数']]
ping=ping[ping['运营商'].isin(['Tim','Wind'])]
ping=ping.groupby(['Offer','运营商']).sum()
ping.to_excel('E:\\2018\\订阅\\二月订阅\\123.xls',\
                  sheet_name='sheet0')
