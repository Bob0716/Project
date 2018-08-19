import pytesseract
from PIL import Image
import os
import time
import pymysql
import compare

def getAllImages_name(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    imageList = os.listdir(folder)
    for i in range(len(imageList)):
        imageList[i] = imageList[i].split('.')
        imageList[i][0] = int(imageList[i][0])
    imageList.sort()
    for j in range(len(imageList)):
        imageList[j][0] = str(imageList[j][0])
        imageList[j] = imageList[j][0] + '.' + imageList[j][1]
    return imageList


def get_allpic_route(s):
    all_route = []
    for i in range(len(s)):
        t = 'f:\\snap\\' + s[i]+'.bmp'
        all_route.append(t)
    return all_route


def segment(im):
    w, h = im.size
    h =int( h / 32)
    #print(int(h))
    im_new = []
    for i in range(32):
        im_pic = im.crop((0, i * h, w, h + h * i))
        w1, h1 = im_pic.size
        w1 = w1 / 3
        im_pic1 = im_pic.crop((0, 0, w1, h1))
        # # im_pic1.show()
        im_pic2 = im_pic.crop((w1, 0, w1 * 2, h1))
        # # im_pic2.show()
        im_pic3 = im_pic.crop((w1 * 2, 0, w1 * 4, h1))
        # im_pic3.show()
        #print(im_pic3.size)#(156, 22)
        # set_to_list = im_pic3.getextrema()
        # print set_to_list
        # set_num=set_to_list[0][1]
        # print set_num

        color = judge_color(im_pic3)
        im_pic_paste = paste_pic(im_pic3)
        #im_pic_paste.show()
        # im_pic_paste.show()
        im_pic1_text=str(print_text3(im_pic1))

        im_pic2_text=str(print_text1(im_pic2))
        im_pic3_text=print_text2(im_pic_paste, color)
        # print_text2(im_pic_paste, color)
        # time1 = time.time()
        im_new.append([im_pic1_text,im_pic2_text]+im_pic3_text)
    return im_new
        # time2 = time.time()
        # print time2 - time1

def segment1(im):
    w, h = im.size
    h = int(h / 32)
    im_new1 = []
    for i in range(31):
        im_pic = im.crop((0, i * h+h-4, w, 2*h + h * i-4))
        w1, h1 = im_pic.size
        w1 = w1 / 3
        im_pic1 = im_pic.crop((0, 0, w1, h1))
        # im_pic1.show()
        im_pic2 = im_pic.crop((w1, 0, w1 * 2, h1))
        # im_pic2.show()
        im_pic3 = im_pic.crop((w1 * 2, 0, w1 * 4, h1))
        # im_pic3.show()

        # print(im_pic3.size)#(88, 22)
        # set_to_list = im_pic3.getextrema()
        # print set_to_list
        # set_num=set_to_list[0][1]
        # print set_num

        color = judge_color(im_pic3)
        im_pic_paste = paste_pic(im_pic3)
        # im_pic_paste.show()
        im_pic1_text=str(print_text3(im_pic1))

        im_pic2_text=str(print_text1(im_pic2))
        im_pic3_text=print_text2(im_pic_paste, color)

        print_text2(im_pic_paste, color)

        im_new1.append([im_pic1_text,im_pic2_text] + im_pic3_text)
    # print im_new
    return im_new1


def judge_color(im_pic):
    set_to_list = list(im_pic.getextrema())
    set_num = set_to_list[0][1]
    if set_num == 0:
        return 'green'
    else:
        return 'red'


def paste_pic(im_pic):
    im_pic.paste(im_test, (78, 0))
    return im_pic
    # im_pic.show()


def print_text1(im_pic):
    text = pytesseract.image_to_string(im_pic, config='-l font')
    return text

def print_text2(im_pic, color):
    text = pytesseract.image_to_string(im_pic, config='-l font')
    li = list(text)
    #print(li)
    if len(li) == 2:
        text = str(li[0])
    else:
        # text=str(li[0:2])
        text = str(li[0]) + str(li[1])
    # print [color,text]
    return [color, text]

def print_text3(im_pic):
    text = pytesseract.image_to_string(im_pic, config='-l font')
    return text

def test_compare(im1_li,im0_li):
        i=0
        # time1=time.time()
        for j in range(len(im1_li)):
            temp1=im1_li[i]
            temp0=im0_li[j]
            if (temp1[0]==temp0[0])and(temp1[1]==temp0[1])and(temp1[2]==temp0[2])and(temp1[3]==temp0[3]):
                i=i+1
            else:
                continue
        if i!=31:
            return im1_li[i:]
        else:
            return 0
                # time2 = time.time()
                # print time2 - time1
        # temp1[j]=temp1[j+1]
def is_empty(l):
    for i in l:
        for j in i:
            if j=='':
                return 1
def renew_time(first_im_li):
    for i in first_im_li:
        # print i[0]
        global str_time
        if len(i[0])==5:
            i[0]=i[0]+':00'
            str_time=i[0][0:5]+':'
        else:
            i[0]=str_time+i[0]
    # print first_im_li
    return first_im_li

im_test = Image.open('b.bmp')
w_test, h_test = im_test.size
# print w_test,h_test#77,22
w_test = w_test / 77
im_test = im_test.crop((w_test * 68, 0, w_test * 75, h_test))
# im_test.show()
# print im_test.size#(8, 22)
s = getAllImages_name("f:\\snap")
route = get_allpic_route(s)#return a list[str element]
#print(route)
first_im=Image.open('f:\\snap\\1503896166.6800728.bmp')
first_im_li=segment(first_im)

im0 = Image.open('f:\\snap\\1503896166.6800728.bmp')
im0_li=segment1(im0)
for i in range(len(route)):
    try:
        print(route[i])
        if i == len(route) - 1:
            break
        pre=None
        if pre is None:
            im1= Image.open(route[i+1])
        if compare.compare(im1,im0)==0:
            continue
        #return a list[list element]
        # time2 = time.time()
        # print time2 - time1
        # print i+1
        im1_li=segment1(im1)
        if is_empty(im1_li):
            continue
        # # test_compare(im2_li, im1_li)
        renew_text=test_compare(im1_li,im0_li)
        im0=im1
        im0_li=im1_li
        # print renew_text
        if renew_text!=0:
            for i in renew_text:
                first_im_li.append(i)
    except:
        print('error!!!!!!!!!!!!!!!!!!!!!!')
        pass
first_im_li=renew_time(first_im_li)
        # print first_im_li
conn=pymysql.Connect(host='127.0.0.1',port=3306,user='root',passwd='geforce460',db='imooc')
cursor=conn.cursor()
print(first_im_li)
f=open('resualt.txt','a+',encoding='utf-8')
f.write(str(first_im_li))
f.close()
for j in first_im_li:
        # print j
    out_time=j[0]
    price=j[1]
    color=j[2]
    transaction=j[3]
    sql = '''insert into pobomn values (\'%s\',%s,\'%s\',%s)''' % (out_time,price,color,transaction)
    # print sql
    cursor.execute(sql)
    conn.commit()
cursor.close()
conn.close()
