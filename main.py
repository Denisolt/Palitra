from PIL import Image
import sys, csv
from resizeimage import resizeimage
import math


def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb

def check(val):
	final = set()
	with open('AcceptedColors.csv') as csvfile:
	    color = csv.reader(csvfile, delimiter=',', quotechar='|')
	    next(color)
	    for row in color:
	        name = (row[0])
	        hexdec = (row[1])
	        for col in val:
	        	if col == hexdec.lower():
		        	final.add(col)
	print final


path = sys.argv[1]

im = Image.open(path)
#im = resizeimage.resize_cover(im, [512, 512])
pix = im.load()
w, h = im.size # breaking the tuple into width and height in px
im = resizeimage.resize_cover(im, [math.sqrt(w), math.sqrt(2)])
s = set() #creating a set
print im.size # Get the width and hight of the image for iterating over

for x in range(0, w):
	for y in range(0, h):
		hex = rgb_to_hex(pix[x,y]) #converting set to hex and storing it
		s.add(hex)

s = sorted(s) #sorting out the s set


check(s)
