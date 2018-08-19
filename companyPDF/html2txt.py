# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import os
import requests
import xlwt

def bs4_paraser(html,route):
    all_value = []
    # value = {}
    soup = BeautifulSoup(html, 'html.parser')
    # soup.prettify()
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    # soup.prettify()
    text=soup.text.strip()

    # print(text)
    # if (soup.text.find("证券代码") != -1):
    #     title = soup.text[:soup.text.find("有限公司")]
    #     print(title)
    # reg1 = re.compile("<[^>]*>")
    # content = reg1.sub('', soup.prettify())
    # print(content.strip())
    # value = soup.text[soup.text.find("证券代码"):soup.text.find("有限公司")]
    # print(value) #<class 'str'>
    # reg=re.compile("..??年.+月.+日")
    # date = reg.findall(text)
    # print(date)
    if(text.find("变更")!= -1):
        htmlname = route[9:-4] + "PDF"
        if(soup.text.find("证券代码")!=-1):
            title = text[:text.find("有限公司")]+"有限公司"
            # title = title.strip()
            text = text[text.find("变更"):]
            # text = text.strip()
        elif(soup.text.find("股票代码")!=-1):
            title = text[:text.find("有限公司")]+"有限公司"
            # title = title.strip()
            text = text[text.find("变更"):]
            # text = text.strip()
        else:
            title = text[:text.find("有限公司")]+"有限公司"
            # title = title.strip()
            text = text[text.find("变更"):]
            # text = text.strip()
        return htmlname+'\n'+title+'\n'+text+'\n'
    else:
        htmlname = route[9:-4]+"PDF"
        return ("未提取PDF为："+htmlname)+'\n'
    # value1 = soup.text[soup.text.find("公告编号"):soup.text.find("公告编号")+ 24]
    # value1 = soup.find("证券代码")
    # print(value)
def getAllFile_name(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    FileList = os.listdir(folder)
    # for i in range(len(FileList)):
    FileList.sort()
    return FileList

def get_allfile_route(FileList):
    all_route = []
    for i in range(len(FileList)):
        t = 'htmlfile/' + FileList[i]
        # print(t)
        all_route.append(t)
    return all_route

def write2excel(return_text,row_num):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('conpanytxt',cell_overwrite_ok=True)
    textlist = return_text.split('\n')
    # print(return_text)
    # for i in textlist:
    #     sheet.write(row_num,0,i)
    #     row_num += 1
    #     book.save('Excel_test.xls')

def main():
    folder = 'htmlfile/'
    FileList = getAllFile_name(folder)
    # print(FileList)
    all_route = get_allfile_route(FileList)
    # print(all_route)
    row_num = 0
    for route in all_route:
         htmlfile = open(route, 'r', encoding="utf-8")
         htmlpage = htmlfile.read()
         htmlfile.close()
         # print(route)
         return_text = bs4_paraser(htmlpage,route) #return_text =
         with open('1.txt', 'a', encoding='utf-8') as f:
             f.write(return_text)
         # write2excel(return_text,row_num)
    # htmlfile = open("1202988876.html", 'r',encoding="utf-8")
    # htmlfile = open("htmlfile\\1202990128.html", 'r', encoding="utf-8")
    # htmlpage = htmlfile.read()
    # bs4_paraser(htmlpage)
    # print all_value

if __name__ == "__main__":
    main()