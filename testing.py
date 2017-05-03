import os,csv
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from PIL import Image
import sys, csv
from resizeimage import resizeimage
import math

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG'])

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


im = Image.open('static/images/image.jpg')
pix = im.load()
w, h = im.size # breaking the tuple into width and height in px
#im = resizeimage.resize_cover(im, [w/2, h/2])
s = set() #creating a set
for x in range(0, w/4):
    for y in range(0, h/4):
        hex = rgb_to_hex(pix[x,y]) #converting set to hex and storing it
        s.add(hex)
s = sorted(s) #sorting out the s set
x = check(s)
print x

@app.route('/', methods=['GET', 'POST'])
def upload_file():
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
            im.save('static/images/image.jpg')
            #w, h = im.size # breaking the tuple into width and height in px
            #im = resizeimage.resize_cover(im, [w/2, h/2])
            #s = set() #creating a set
            #for x in range(0, w/2):
            #    for y in range(0, h/2):
            #        hex = rgb_to_hex(pix[x,y]) #converting set to hex and storing it
            #        s.add(hex)
            #s = sorted(s) #sorting out the s set
            #x=check(s)
            #print x
        return redirect(url_for('upload_file',filename=filename))
    return render_template('index.html', x = x)


if __name__ == '__main__':
   app.run(debug = True)
