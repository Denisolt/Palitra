from PIL import Image
import sys

path = sys.argv[1]

im = Image.open(path)
pix = im.load()
w, h = im.size
print im.size #Get the width and hight of the image for iterating over
print pix[5,5] #Get the RGBA Value of the a pixel of an image
