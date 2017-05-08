import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy as np

def getcol(codes, NUM_CLUSTERS):
	s = set()
	for c in range(0, NUM_CLUSTERS):
		peak = codes[c]
		peak = peak.astype(int)
		colour = ''.join(format(c, '02x') for c in peak)
		final = ('#%s' % colour)
		s.add(final)
	return s

NUM_CLUSTERS = 7

print('reading image')
im = Image.open('image.jpg')
im = im.resize((150, 150))

ar = scipy.misc.fromimage(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2])
#print ('finding clusters')
#print(ar)
#print("Variable type:", type(ar))
codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)
#print('cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

print scipy.histogram(vecs, len(codes))
s = set()
s = counts

#index_max = scipy.argmax(counts)
#print 'max index',index_max              # To return the one and only max value
#peak = codes[index_max]

#peak = peak.astype(int)
#colour = ''.join(format(c, '02x') for c in peak)
#print colour
x = set()
x = getcol(codes, NUM_CLUSTERS)
print x