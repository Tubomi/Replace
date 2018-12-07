i=[1,2,3,4,5,'a','b','a',6,7,8,9,10,11,12,13,14,15,16,17]
total=[]
import random
for x in range(901):
    star=[]
    t=0
    while True:
        z=random.choice(i)
        star.append(z)
        t=t+1
        if 'a' in star and 'b' in star:
            #print(star)
            #print(t)
            total.append(t)
            break
        
#print(total)
s=sum(total)/len(total)
print(s)

