import matplotlib.pyplot as plt
import datetime

f=open('resualt.txt','r',encoding='utf-8')
first_im_li=f.read()
f.close()
first_im_li=eval(first_im_li)
time_s=[]
price_s=[]
for i in first_im_li:
    time=datetime.datetime.strptime(i[0],'%H:%M:%S')
    price=i[1]
    time_s.append(time)
    price_s.append(price)
plt.plot(time_s,price_s)
plt.show()