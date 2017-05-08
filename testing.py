import os,csv
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy as np

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def getcol(codes, NUM_CLUSTERS):
    s = set()
    for c in range(0, NUM_CLUSTERS):
        peak = codes[c]
        peak = peak.astype(int)
        colour = ''.join(format(c, '02x') for c in peak)
        final = ('#%s' % colour)
        s.add(final)
    return s

NUM_CLUSTERS = 5
im = Image.open('static/images/image.jpg')
im = im.resize((150, 150))

ar = scipy.misc.fromimage(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2])
codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences
s = set()
s = counts

x = set()
x = getcol(codes, NUM_CLUSTERS)
print x

def GetnewColors():
    NUM_CLUSTERS = 7
    im = Image.open('static/images/image.jpg')
    im = im.resize((150, 150))

    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])
    codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences
    s = set()
    s = counts

    x = set()
    x = getcol(codes, NUM_CLUSTERS)
    return x

@app.route('/', methods=['GET', 'POST'])
def upload_file(x=x):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            im = Image.open(file.filename)
            pix = im.load()
            im = im.resize((150, 150))
            x = GetnewColors()
        return render_template('index.html', x = x)
    x = GetnewColors()
    return render_template('index.html', x = x)


if __name__ == '__main__':
   app.run(debug = True)
