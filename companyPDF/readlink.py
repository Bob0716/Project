import re
import requests
import argparse,os
from fake_useragent import UserAgent
ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

def getPdfUrl(root_url):
    response = requests.get(root_url, headers=headers)
    ## 如果requests没有从页面中获得字符编码，那么设置为utf-8
    # print(response.text)
    regcode = r'[84]\d{5}[\s]'
    code_re = re.compile(regcode)
    code_value = re.findall(code_re,response.text)
    # print(code_value)
    if(code_value==[]):
        reg=r'http://www.cninfo.com.cn/finalpage/?.+\d+.PDF'
        # reg_name = r'\d+ \D+'
        url_re=re.compile(reg)
        url_value=re.findall(url_re,response.text)
        print(url_value)
    else:
        return 1
    # return url_value,reg_name
    return url_value

## 下载pdf
def savePdf(url,pdf_name):
    response = requests.get(url,headers=headers,stream=True)
    ## 如果指定的文件夹，那么便新建
    if not os.path.exists('D:\pdf'):
        os.makedirs('D:\pdf')
    ## os.path.join(a,b..)如果a字符串没有以/结尾，那么自动加上\\。（windows下）
    with open(os.path.join('D:\pdf',pdf_name),"wb") as pdf_file:
        for content in response.iter_content():
            pdf_file.write(content)
def main():
    with open('2.txt') as f:
        lines = f.readlines() # 读取文本中所有内容，并保存在一个列表中，列表中每一个元素对应一行数据
        for line in lines:
            print(line.rstrip())
            url_value = getPdfUrl(line.rstrip())
            if (url_value==1):
                continue
            # print(type(url_value))
            # url_value, = getPdfUrl('http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/bulletin_detail/true/1203494652?announceTime=2017-03-30')
            # url_value, = getPdfUrl('http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/bulletin_detail/true/1205039405?announceTime=2018-06-05')
            # url_value, = getPdfUrl('http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/bulletin_detail/true/1205032587?announceTime=2018-06-04%2015:48')
            # print(url_value)
            if(url_value!=[]):
                url_value="".join(url_value)
                pdf_name=url_value.split("/")
                # print(pdf_name)
                print(pdf_name+pdf_name[-1])
                # savePdf(url_value,pdf_name=pdf_name[-1])
            else:
                print("没有PDF文件")
        # print(url_pdfName)
        # print(lines) # 每一行数据都包含了换行符
# response=requests.get()
if __name__ == "__main__":
    main()
