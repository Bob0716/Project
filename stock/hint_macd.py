import pandas as pd
import datetime
import numpy as np
def last(current_time,rdf,k):
    time_delta=datetime.timedelta(seconds=k*60)
    shape=rdf.shape
    length=shape[0]
    for i in range(length):
        if i==length-1:
            return rdf['1'][i]
        elif rdf['0'][i]<=current_time and rdf['0'][i+1]>current_time:
            return rdf['1'][i]
def get_MACD(current_index,tdf,rdf,k):
    if pd.isnull(tdf[str(k)+'m'][current_index])==False:
        print(tdf[str(k)+'m'][current_index])
        return tdf[str(k)+'m'][current_index]
    if current_index<=k*60:
        EMA12=last(tdf['time'][current_index],rdf,k)
        EMA26=last(tdf['time'][current_index],rdf,k)
        tdf['EMA12'+str(k)][current_index]=EMA12
        tdf['EMA26'+str(k)][current_index] = EMA26
        DIFF=EMA12-EMA26
        DEA=DIFF*0.2
        tdf['DEA' + str(k)][current_index] = DEA
        return 2*(DIFF-DEA)
    else:
        EMA12 = last(tdf['time'][current_index], rdf,k) * (2 / 13)+tdf['EMA12'+str(k)][current_index-k*60]*(11 / 13)
        EMA26 = last(tdf['time'][current_index],rdf, k) * (2 / 27)+tdf['EMA26'+str(k)][current_index-k*60]*(25 / 27)
        tdf['EMA12'+str(k)][current_index] = EMA12
        tdf['EMA26'+str(k)][current_index] = EMA26
        DIFF = EMA12 - EMA26
        DEA = DIFF * 0.2+0.8*tdf['DEA' + str(k)][current_index-k*60]
        tdf['DEA' + str(k)][current_index] = DEA
        return 2*(DIFF-DEA)
df=pd.read_csv('record.csv',index_col=0)
df_time=pd.read_csv('time_df.csv',index_col=0)
print(df_time)
df_time['EMA123']=None
df_time['EMA263']=None
df_time['EMA121']=None
df_time['EMA261']=None
df_time['EMA1215']=None
df_time['EMA2615']=None
df_time['DEA1']=None
df_time['DEA3']=None
df_time['DEA15']=None
#print(df_time)
#print(get_MACD(0,df_time,df,3))
sp=df_time.shape
for i in range(sp[0]):
    print(i)
    df_time['1m'][i]=get_MACD(i,df_time,df,1)
    df_time['3m'][i] = get_MACD(i, df_time, df, 3)
    df_time['15m'][i]= get_MACD(i, df_time, df, 15)
print(df_time)
df_time.to_csv('MACD4.csv')