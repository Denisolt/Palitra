# Palitra
![alt tag](https://raw.githubusercontent.com/Denisolt/Palitra/master/readmeImage.jpg)</br>
## Project Scope:
This project lets user upload any pictureand displays 7 most used colors. The inspiration came from Wes Anderson's movies, particulary from "The Grand Budapest Hotel". This project is written in Python, using Pillow to work with images, Numpy and Scipy to create clusters of colors and sort them out, Flask is used in order to create a web application. As always I have used a free template provided by freehtml5.co. Right now it is hosted on heroku: https://palitra.herokuapp.com
## Inspiration:
![alt tag](http://anotherimg.dazedgroup.netdna-cdn.com/706/azure/another-prod/300/0/300557.jpg)</br>
I was very impressed with the colors that movie director - Wes Anderson used, so I decided to create this application. 

## Installation:
Downloading the project:
```bash
git clone https://github.com/Denisolt/Palitra.git
cd Palitra-master

```
Activation of virtual environment:
```bash
source local/bin/activate
pip install -r /path/to/requirements.txt
```
## Execution:
```bash
python main.py
```
## Next Steps:
- Implementing web cam upload (thanks to Chaya Levin for the idea)
- Implementing the return of RGBA value of a pixel that user points at (thanks to Timmy for the idea)

## Things to fix:
- some html work, since I hate front end development
- add the actual hex or rgba values next to each color circle
