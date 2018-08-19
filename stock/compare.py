from PIL import Image
from PIL import ImageChops
from PIL import ImageDraw
def compare(A,B):
    dif = ImageChops.difference(A, B).getbbox()
    print(dif)
    if dif==None:
        return 0
    else:
        return 1
# draw = ImageDraw.Draw(imageB)
# draw.rectangle(dif)
# imageB.show()