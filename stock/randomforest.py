from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
import MACD2DATA
from matplotlib.lines import Line2D
def roc(t2,y,min,max,step):
    t=t2
    TPR_list=[]
    FPR_list=[]
    for i in range(int((max-min)/step)):
        t=np.copy(t2)
        print(t2)
        t[t < min+i*step] = -1
        t[t >= min+i*step] = 1
        (TP, TN, FN, FP)=correct(test_y, t)
        TPR=TP/(TP+FN)
        FPR=FP/(FP+TN)
        TPR_list.append(TPR)
        FPR_list.append(FPR)
    print(TPR_list,FPR_list)
    line1 = [(0, 0), (1, 1)]
    figure, ax = plt.subplots()
    ax.add_line(Line2D((0,1),(0,1),linewidth=1, color='blue'))
    ax.scatter(FPR_list,TPR_list)
    plt.show()
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

rf = RandomForestClassifier(n_estimators=100)
rf.fit( train_x,train_y)
t = rf.predict(test_x)
# t=np.round(t)
# t[t<0.3]=-1
# t[t>=0.3]=1
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(test_y, '.',color='red', lw=2)
plt.plot(t,  '.',color='green', lw=2)
plt.show()
# print(t)
print(correct(test_y,t))
#roc(t,test_y,-1,1,0.05)
print(rf.estimators_)
#print(rf.classes_)
#print(rf.n_classes_)
print(rf.feature_importances_)