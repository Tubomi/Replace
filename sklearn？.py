import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
x = np.linspace(0,8,10)
np.random.seed(1)
y = 400+np.random.random(10)*400+x*0.002
print(x)
print(y)
np.random.seed?
lr2.fit(x.reshape(-1,1),y_2)
y_hat_2 = lr2.predict(x.reshape(-1,1))
y_1_random = (y-x*0.002)
y_2 = np.mean(y_1_random) + x * 0.002 + (y_1_random-np.mean(y_1_random))/400*20

plt.figure(figsize=[8,6])
plt.scatter(x,y_2,s=0.2)
plt.xlabel('PM_Nongzhonguan')
plt.ylabel('PM_Dongsi')
plt.ylim([400,800])
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
x = np.linspace(0,800,10000)
np.random.seed(1)
y = 400+np.random.random(10000)*400+x*0.002
plt.figure(figsize=[8,6])
plt.scatter(x,y,s=0.2)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x.reshape(-1,1),y)
y_hat = lr.predict(x.reshape(-1,1))
print(y_hat)
