from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import scipy.io as sio
import matplotlib.pyplot as plt
import MACD2DATA
import numpy as np
def build_model(length,width):
    model=Sequential()
    model.add(LSTM(units=200,input_shape=[length,width]))
    model.add(Dense(200,activation='tanh'))
    model.add(Dense(1))
    model.compile(loss='mse',optimizer='adam')
    return model
MACD,record=MACD2DATA.init_data()
length=180
width=3
ratio=0.7
x_list,y_list=MACD2DATA.data(MACD,record,length)
x_list=x_list
#print(x_list.shape,y_list.shape)
train_size=int(y_list.shape[0]*ratio)
train_x=x_list[:train_size]
test_x=x_list[train_size:]
train_y=y_list[:train_size]
test_y=y_list[train_size:]
print(train_y.shape,test_y.shape)

model = build_model(length, width)
model.fit(train_x, train_y, batch_size=10, epochs=2, validation_split=0.1)
result = model.predict(test_x)
result=result
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(test_y, color='red', lw=2)
plt.plot(result, color='green', lw=2)
plt.show()
print(type(result))
sio.savemat('Mat.mat',{'train_x':train_x,'train_y':train_y,'test_x':test_x,'test_y':test_y})
np.save('train_x',train_x)
np.save('train_y',train_y)
np.save('test_x',test_x)
np.save('test_y',test_y)
# print('Regression Score: %.6f' % r2_score(y_test, result))
# print('error rate:%.6f' % error(y_test, result))
# print('-------------------------------------')