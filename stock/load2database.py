import pymysql
conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='geforce460',db='imooc')
cursor=conn.cursor()
f=open('resualt.txt','r',encoding='utf-8')
first_im_li=f.read()
f.close()
first_im_li=eval(first_im_li)
for j in first_im_li:
    try:
        #print(j)
        out_time=j[0]
        price=j[1]
        color=j[2]
        transaction=j[3]
        sql = '''insert into pobomn values (\'%s\',%s,\'%s\',%s)''' % (out_time,price,color,transaction)
    # print sql
        cursor.execute(sql)
        conn.commit()
    except:
        print('error')
        print(j)
        pass
cursor.close()
conn.close()