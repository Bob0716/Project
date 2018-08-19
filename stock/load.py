import pandas as pd
import datetime
def strp(s,format='%H:%M:%S'):
    return datetime.datetime.strptime(s,format)
def load2csv(file):
    second_delta = datetime.timedelta(seconds=1)
    f = open(file, 'r', encoding='utf-8')
    first_im_li = f.read()
    f.close()
    first_im_li = eval(first_im_li)
    df = pd.DataFrame(first_im_li)
    shape = df.shape
    time_df = pd.DataFrame(columns=['1m', '3m', '15m'])
    # print(time_df)
    start = df[0][0]
    end = df[0][shape[0] - 1]
    df[0] = df[0].apply(strp)
    start = datetime.datetime.strptime(start, '%H:%M:%S')
    end = datetime.datetime.strptime(end, '%H:%M:%S')
    print(start, type(end))
    tmp = start
    time_s = []
    while (tmp <= end):
        time_s.append(tmp)
        tmp = tmp + second_delta
    time_df['time'] = time_s
    print(df)
    df.to_csv('record.csv')
    time_df.to_csv('time_df.csv')