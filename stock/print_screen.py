# __author__:"Adolphus"
# project:'stock'
from PIL import ImageGrab
import time

def grab(geo,fre):
    while(1):
        current_time=time.time()
        im = ImageGrab.grab(geo)
        im.save('F:/snap/'+str(current_time)+'.bmp', 'bmp')
        if fre==0:
            break
        time.sleep(fre)
# geo=(503,127, 790, 180)
# grab(geo)
# time.sleep(4)
# for i in range(5):
#     time.sleep(1)
#     grab(geo)