import os,csv
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

from PIL import Image
import sys, csv
from resizeimage import resizeimage
import math


UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    return final

@app.route('/', methods=['GET', 'POST'])
def upload_file(x=None):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print 'file empty'
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print 'file approved'
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            im = Image.open(file.filename)
            #im = resizeimage.resize_cover(im, [512, 512])
            pix = im.load()
            im.save('static/images/image.jpg')
            w, h = im.size # breaking the tuple into width and height in px
            im = resizeimage.resize_cover(im, [w/2, h/2])
            s = set() #creating a set
            for x in range(0, w):
                for y in range(0, h):
                    hex = rgb_to_hex(pix[x,y]) #converting set to hex and storing it
                    s.add(hex)

            s = sorted(s) #sorting out the s set

            x=check(s)
            print x
            return redirect(url_for('upload_file',filename=filename, x=x))
  
    return render_template('index.html',x=x)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug = True)
