# __author__:"Adolphus"
# project:'stock'
import pytesseract
from PIL import Image,ImageEnhance
import os
for file in os.listdir('snap'):
    print(file)
    image = Image.open('snap/'+file)
    vcode = pytesseract.image_to_string(image)
    print (vcode)
# image = Image.open('D:\work\代码&程序\stock\snap\\test.jpeg')
# vcode = pytesseract.image_to_string(image)
# print (vcode)