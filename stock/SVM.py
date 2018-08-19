import matplotlib.pyplot as plt
import MACD2DATA
import numpy as np
from sklearn.svm import NuSVC
def correct(real,predict):
    TP=0
    TN=0
    FN=0
    FP=0
    for i in range(len(real)):
        if real[i]==1 and predict[i]==1:
            TP+=1
        elif real[i]==-1 and predict[i]==-1:
            TN+=1
        elif real[i] == 1 and predict[i] == -1:
            FN += 1
        elif real[i]==-1 and predict[i]==1:
            FP+=1
    return (TP,TN,FN,FP)

MACD,record=MACD2DATA.init_data()
length=60
width=3
ratio=0.7
x_list,y_list=MACD2DATA.data_SVM_velocity(MACD,record,length)
#x_list=x_list[:,0,:]
print(x_list.shape)
print(y_list.shape)
#print(x_list.shape,y_list.shape)
train_size=int(y_list.shape[0]*ratio)
train_x=x_list[:train_size]
test_x=x_list[train_size:]
train_y=y_list[:train_size]
test_y=y_list[train_size:]
for i in range(8):
    clf = NuSVC(nu=i*0.1+0.1)
    clf.fit(train_x, train_y)
    y = clf.predict(test_x)
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.plot(test_y, '.',color='red', lw=2)
    # plt.plot(y,  '.',color='green', lw=2)
    # plt.show()
    print(test_y.sum())
    print(correct(test_y, y))