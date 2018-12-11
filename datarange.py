import numpy as np
import pandas as pd
import random
b=[]
for i in range(1,366):
    a=random.randint(1,1000)
    x=28500+i*4000-i*4000*0.2+a
    b.append(x)
Z=range(3500,5400) 
z=random.sample(Z,365)#可以从指定的序列中，随机的截取指定长度的片断，不作原地修改
import matplotlib.pyplot as plt
dates = pd.date_range('20180101', periods=365)#设置时间列表
plt.plot(b)
test=pd.DataFrame({'active':b,'new':z},index=dates)
#test.to_excel('E:\\2018\\test-.xls',sheet_name='sheet0')
