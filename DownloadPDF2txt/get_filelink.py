import requests
from bs4 import BeautifulSoup
import re
import json
import time
# content={'code':'notautosubmit'}
# r = requests.get('http://www.cninfo.com.cn/cninfo-new/fulltextSearch',params=content)
# print(r.url)
#print(r.encoding)
#print(r.json())
#print(r.content)
# print(r.text)
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.cninfo.com.cn/cninfo-new/fulltextSearch?code=&notautosubmit=&keyWord=%E7%BB%8F%E8%90%A5%E8%8C%83%E5%9B%B4%E5%8F%98%E6%9B%B4') #经营范围变更
# driver.get('http://www.cninfo.com.cn/cninfo-new/fulltextSearch?code=&notautosubmit=&keyWord=%E4%B8%BB%E8%90%A5%E4%B8%9A%E5%8A%A1%E5%8F%98%E6%9B%B4')  #主营业务变更
element = driver.find_element_by_id("rangeA")
element.clear()
element.send_keys("2017-01-01 ~ 2017-06-02")
driver.find_element_by_class_name("search-a").click()

while(1):
    time.sleep(2)
    elelist = driver.find_element_by_xpath("//*[@id='ul_a_title']").find_elements_by_tag_name("a")
    for ele in elelist:
        i=ele.get_attribute("href")
        print(i)
        # filename = '经营范围变更20170603-20180603.txt'
        # filename = '主营业务变更20170101-20170602.txt'
        filename = '经营范围变更20170101-20170602.txt'
        with open(filename, 'a') as f:  # 如果filename不存在会自动创建，写之前会清空文件中的原有数据！
            f.write(i+'\n')
    driver.find_element_by_class_name("next").click()
        # response = requests.get(i)
        # brower=webdriver.Chrome()
        # brower.get(i)
        # brower.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/div/a").click()
        # time.sleep(3)
        # brower.close()

# links = driver.find_elements_by_tag_name("a")

# response = requests.get(url)
# response.text

# print(response.cookies)
# result = response.read()
# result.decode('utf-8')
# jsonData = json.loads(result)
# print(jsonData)
# print(url)
# for link in driver.find_elements_by_tag_name("a"):
#     print(link.get_attribute("href"))
# driver.close()
# ele=driver.find_element_by_id("con-div-a-title").text
# print(ele)
