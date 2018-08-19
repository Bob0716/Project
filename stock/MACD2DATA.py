import pandas as pd
import datetime
import numpy as np
def init_data(MACD='MACD4.csv',record='record.csv'):
    raw_MACD=pd.read_csv(MACD)
    raw_record=pd.read_csv(record)
    raw_MACD['time']=pd.to_datetime(raw_MACD['time'],format='%Y-%m-%d %H:%M:%S')
    return raw_MACD,raw_record
def sqe(time,MACD,target,length):
    time=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    delta=datetime.timedelta(seconds=length)
    start=time-delta
    sq=MACD[MACD['time']>start]
    sq=sq[sq['time']<=time]
    sq=sq.reset_index()
    m1=list(sq['1m'])
    m3=list(sq['3m'])
    m15=list(sq['15m'])
    sq=[m1,m3,m15]
    sq=np.array(sq)
    sq=np.reshape(sq,(length,3))
    #print(sq)
    return (sq,target)
def data(raw_MACD,raw_record,length=60):
    shape=raw_record.shape[0]

    sq_list=[]
    t_list=[]
    for i in range(shape-1-length):
        i = i + length
        time = raw_record['0'][i]
        target = raw_record['1'][i] - raw_record['1'][i + 1]
        if target > 0:
            target = 1
        elif target < 0:
            target = -1
        #print(time, target)
        (sq, t) = sqe(time, raw_MACD, target, length)
        sq_list.append(sq)
        t_list.append(t)
    sq_list = np.array(sq_list)
    t_list=np.array(t_list)
    return (sq_list,t_list)
def sqe_SVM(time,MACD,target,length):
    time=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    delta=datetime.timedelta(seconds=length)
    start=time-delta
    sq=MACD[MACD['time']>start]
    sq=sq[sq['time']<=time]
    sq=sq.reset_index()
    m1=list(sq['1m'])
    m3=list(sq['3m'])
    m15=list(sq['15m'])
    sq=[m1,m3,m15]
    sq=np.array(sq)
    sq=np.reshape(sq,(length*3))
    #print(sq)
    return (sq,target)
def data_SVM(raw_MACD,raw_record,length=60):
    shape=raw_record.shape[0]

    sq_list=[]
    t_list=[]
    for i in range(shape-1-length):
        i = i + length
        time = raw_record['0'][i]
        target = raw_record['1'][i] - raw_record['1'][i + 1]
        if target >=0:
            target = 1
        elif target <0:
            target = -1
        #print(time, target)
        (sq, t) = sqe_SVM(time, raw_MACD, target, length)
        sq_list.append(sq)
        t_list.append(t)
    sq_list = np.array(sq_list)
    t_list=np.array(t_list)
    return (sq_list,t_list)
def data_SVM_velocity(raw_MACD,raw_record,length=60):
    shape=raw_record.shape[0]

    sq_list=[]
    t_list=[]
    for i in range(shape-1-length):
        i = i + length
        time = raw_record['0'][i]
        target = raw_record['1'][i] - raw_record['1'][i + 1]
        if target >=0:
            target = 1
        elif target <0:
            target = -1
        #print(time, target)
        (sq, t) = velocity_SVM(time, raw_MACD, target, length)
        sq_list.append(sq)
        t_list.append(t)
    sq_list = np.array(sq_list)
    t_list=np.array(t_list)
    return (sq_list,t_list)
def velocity_SVM(time,MACD,target,length):
    time=datetime.datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    delta=datetime.timedelta(seconds=1)
    start=time-delta
    sq=MACD[MACD['time']==start]
    sq=sq.reset_index()
    sq1=MACD[MACD['time']==time]
    sq1 = sq1.reset_index()
    sq2 = MACD[MACD['time'] == start-delta]
    sq2 = sq2.reset_index()
    m1=sq['1m'][0]-sq1['1m'][0]
    m3=sq['3m'][0]-sq1['3m'][0]
    m15=sq['15m'][0]-sq1['15m'][0]
    sq=[m1,m3,m15,sq['1m'][0],sq['3m'][0],sq['15m'][0]]
    m12 = sq1['1m'][0] - sq2['1m'][0]-m1
    m32 = sq1['3m'][0] - sq2['3m'][0]-m3
    m152 = sq1['15m'][0] - sq2['15m'][0]-m15
    sq.extend([m12,m32,m152,])
    sq=np.array(sq)
    # sq=np.reshape(sq,(length*3))
    #print(sq)
    return (sq,target)