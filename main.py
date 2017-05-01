from PIL import Image
import sys



#for debug printing the size of the set
#print len(s)

def rgb_to_hex(rgb):
	return '%02x%02x%02x' % rgb


path = sys.argv[1]

im = Image.open(path)
pix = im.load()
w, h = im.size #braking the tuple into width and height in px
s = set()
print im.size #Get the width and hight of the image for iterating over
#print pix[5,5] #Get the RGBA Value of the a pixel of an image

for x in range(0, w):
	for y in range(0, h):
		hex = rgb_to_hex(pix[x,y])
		s.add(hex)

s = sorted(s)

print s
